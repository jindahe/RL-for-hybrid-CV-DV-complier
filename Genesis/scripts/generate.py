from itertools import permutations

nums = ['+2', '-0', '-0', '-0']

seen = set()
res = []

for p in permutations(nums, 4):
    if p in seen:
        continue
    seen.add(p)
    s = "[" + "".join(str(x) for x in p) + "]"  + ", 2, 1, 40, 8, 48, 27, 179,"
    res.append(s)

for s in res:
    print(s)
