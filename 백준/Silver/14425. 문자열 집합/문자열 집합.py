N, M = map(int, input().split())
S = [input() for _ in range(N)]
print(sum([(input() in S) for _ in range(M)]))
