from itertools import permutations
import numpy as np

nums = ['+3', '+1', '-0', '-0']

seen = set()
res = []

for p in permutations(nums, len(nums)):
    if p in seen:
        continue
    seen.add(p)
    s = "[" + "".join(str(x) for x in p) + "]"  + ", 42, 2, 800, 148, 948, 434, 3170,"
    res.append(s)

for s in res:
    print(s)
