from itertools import permutations

with open("datasets/rosalind_perm.txt") as f:
    n = int(f.read().strip())

l = [i for i in range(1, n + 1)]

perm = list(permutations(l))

print(len(perm))
for p in perm:
    print(*p)
