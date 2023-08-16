N, M = map(int, input().split())
바구니 = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i-1, j):
        바구니[n] = k

print(*바구니)