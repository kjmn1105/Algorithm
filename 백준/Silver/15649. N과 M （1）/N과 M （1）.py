import itertools

N, M = map(int, input().split())
for p in sorted(list(itertools.permutations(range(1, N+1), M))):
    print(*p)