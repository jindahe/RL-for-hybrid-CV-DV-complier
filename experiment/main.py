import os
import numpy as np
import sys
import pandas as pd
import ast  # 用于安全解析文本中的列表字符串

# 导入自定义模块
try:
    from kernel import compute_integer_nullspace
    # 尝试导入 5 变量预测模块
    try:
        from predict_5 import HighPrecisionQuantumPredictor
    except ImportError:
        # 如果找不到 predict_5，尝试从 predict_4 导入 (防止文件名没改)
        from predict_4 import HighPrecisionQuantumPredictor
        
except ImportError as e:
    print("错误: 无法导入 kernel 或 predict 模块。请确保它们在同一目录下。")
    print(f"详细信息: {e}")
    sys.exit(1)

def parse_txt_params(txt_path):
    """
    解析 problem_params.txt 文件
    提取: 问题编号, 约束数, 约束矩阵 A
    """
    problem_id = 0
    constraint_num = 0  # 初始化约束数
    A_matrix = None
    
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                
                # 提取问题编号
                if line.startswith("问题编号"):
                    parts = line.split(":")
                    if len(parts) > 1:
                        problem_id = int(parts[1].strip())

                # ================= 新增: 提取约束数 =================
                elif line.startswith("约束数"):
                    # 假设格式为 "约束数: 2"
                    parts = line.split(":")
                    if len(parts) > 1:
                        try:
                            constraint_num = int(parts[1].strip())
                        except ValueError:
                            print(f"  警告: 无法解析约束数: {line}")
                # ===================================================
                        
                # 提取矩阵 A
                elif line.startswith("约束矩阵 A"):
                    parts = line.split("=")
                    if len(parts) > 1:
                        matrix_str = parts[1].strip()
                        try:
                            list_data = ast.literal_eval(matrix_str)
                            A_matrix = np.array(list_data)
                        except:
                            print(f"  警告: 无法解析矩阵字符串: {matrix_str}")
                            
    except Exception as e:
        print(f"  读取文件出错: {e}")
        return None, None, None

    return problem_id, constraint_num, A_matrix

def process_txt_and_predict(root_data_dir, model_csv_path, output_csv_path):
    # 1. 初始化预测器
    print(f"正在初始化预测模型 (CSV路径: {model_csv_path})...")
    if not os.path.exists(model_csv_path):
        print(f"错误: 找不到模型训练文件: {model_csv_path}")
        return

    predictor = HighPrecisionQuantumPredictor(csv_path=model_csv_path)
    
    if not predictor.is_trained:
        print("模型训练失败，退出。")
        return

    print("模型加载完成。开始扫描 .txt 文件 (5变量版本 + 约束数提取)...")
    print("="*60)

    all_results = []
    file_count = 0
        
    # 2. 遍历文件夹
    for dirpath, dirnames, filenames in os.walk(root_data_dir):
        target_file = 'problem_params.txt'
        
        if target_file in filenames:
            txt_path = os.path.join(dirpath, target_file)
            file_count += 1
            print(f"处理文件 [{file_count}]: {txt_path}")
            
            # 3. 解析 TXT 获取 A, Problem_ID 和 约束数
            p_id, c_num, A_matrix = parse_txt_params(txt_path)
            
            if A_matrix is None:
                print("  -> 跳过: 未找到矩阵 A 或解析失败")
                continue
            
            if A_matrix.ndim == 1:
                A_matrix = A_matrix.reshape(1, -1)
            
            try:
                # 4. 计算 Kernel 向量
                basis_vectors = compute_integer_nullspace(A_matrix)
                
                # 5. 预测并收集结果
                for idx, vec in enumerate(basis_vectors):
                    if len(vec) != 5:
                        print(f"    -> 跳过: 向量维度 {len(vec)} 不等于 5")
                        continue
                    
                    a, b, c, d, e_val = vec
                    
                    res = predictor.predict(a, b, c, d, e_val)
                    
                    row_data = {
                        'Problem_ID': p_id,
                        'Constraint_Num': c_num,  # 保存约束数
                        'Vector_Index': idx + 1,
                        'a': a, 'b': b, 'c': c, 'd': d, 'e': e_val,
                        'Single_Gate': res.get('single_gate'),
                        'Two_Gate': res.get('two_gate'),
                        'Total_Gate': res.get('total_gate'),
                        'Depth': res.get('depth'),
                        'Latency': res.get('latency')
                    }
                    all_results.append(row_data)
                    print(f"    -> Vec {idx+1}: {vec} | Total: {res.get('total_gate')}")

            except Exception as ex:
                print(f"  -> 计算出错: {ex}")

    print("="*60)
    
    if not all_results:
        print("未生成任何结果数据。")
        return

    # 6. 处理数据并保存 (详细版)
    print("正在处理和保存详细数据...")
    df = pd.DataFrame(all_results)
    
    # 排序
    df['Problem_ID'] = pd.to_numeric(df['Problem_ID'], errors='coerce').fillna(0).astype(int)
    
    # 定义列顺序，把 Constraint_Num 加进去
    cols_order = ['Problem_ID', 'Constraint_Num', 'Vector_Index', 
                  'a', 'b', 'c', 'd', 'e', 
                  'Single_Gate', 'Two_Gate', 'Total_Gate', 'Depth', 'Latency']
    
    # 确保列存在再排序
    existing_cols = [c for c in cols_order if c in df.columns]
    df = df[existing_cols]
    
    # 按 Problem_ID 和 Vector_Index 排序
    df = df.sort_values(by=['Problem_ID', 'Vector_Index'], ascending=[True, True])
    
    df.to_csv(output_csv_path, index=False, encoding='utf-8')
    print(f"详细结果已保存至: {output_csv_path}")

    # 7. 生成聚合版 (Problem_ID 相加)
    print("正在生成聚合数据 (Sum by Problem_ID)...")
    cols_to_sum = ['Depth', 'Single_Gate', 'Two_Gate']
    
    # 修改聚合逻辑：按 Problem_ID 和 Constraint_Num 分组
    # 这样 Constraint_Num 会保留在结果中（因为它对同一个 Problem_ID 是唯一的）
    df_agg = df.groupby(['Problem_ID', 'Constraint_Num'])[cols_to_sum].sum().reset_index()
    
    agg_csv_path = output_csv_path.replace('.csv', '_aggregated.csv')
    df_agg.to_csv(agg_csv_path, index=False, encoding='utf-8')
    print(f"聚合结果已保存至: {agg_csv_path}")

if __name__ == "__main__":
    # ================= 配置区域 =================
    
    # 1. 数据根目录 (txt 所在文件夹)
    DATA_ROOT_DIR = '/Users/jinboyu/Documents/GitHub/RL-for-hybrid-CV-DV-complier/experiment/5_1/' 
    
    # 2. 训练用 CSV 路径 (5变量版本)
    MODEL_CSV_PATH = '/Users/jinboyu/Documents/GitHub/RL-for-hybrid-CV-DV-complier/experiment/five/result_logic_[abcde].csv'
    
    # 3. 输出结果 CSV 的保存路径
    OUTPUT_CSV_PATH = '/Users/jinboyu/Documents/GitHub/RL-for-hybrid-CV-DV-complier/experiment/5_1.csv'
    
    # ===========================================
    
    process_txt_and_predict(DATA_ROOT_DIR, MODEL_CSV_PATH, OUTPUT_CSV_PATH)