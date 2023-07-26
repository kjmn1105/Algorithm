N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
result = [[0]*M for _ in range(N)]

for j in range(N):
    for i in range(M):
        result[j][i] = A[j][i] + B[j][i]
    print(*result[j])