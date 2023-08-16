import sys
input = sys.stdin.readline

N, M = map(int, input().split())
바구니 = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(lambda x: x-1, map(int, input().split()))
    바구니[i], 바구니[j] = 바구니[j], 바구니[i] 

print(*바구니)