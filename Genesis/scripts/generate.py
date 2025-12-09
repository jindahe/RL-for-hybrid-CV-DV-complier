from itertools import permutations
import numpy as np

nums = ['-1', '-1', '+1', '+1']

seen = set()
res = []

for p in permutations(nums, len(nums)):
    if p in seen:
        continue
    seen.add(p)
    s = "[" + "".join(str(x) for x in p) + "]"  + ", 42, 4, 790, 158, 948, 226, 1442"
    res.append(s)

for s in res:
    print(s)
