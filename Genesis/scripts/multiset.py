from itertools import product

def patterns(m):
    """Return all multiset-types of (a,b,c,d) with |a|+|b|+|c|+|d| = m."""
    reps = set()
    for a, b, c, d in product(range(-m, m+1), repeat=4):
        if abs(a) + abs(b) + abs(c) + abs(d) != m:
            continue
        rep = tuple(sorted((a, b, c, d)))
        reps.add(rep)
    return sorted(reps)

for r in patterns(4):
    print(r)
