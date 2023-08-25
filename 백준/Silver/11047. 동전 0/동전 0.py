import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input().rstrip()) for _ in range(N)]
cnt = 0

for c in sorted(coins, reverse=True):
    if K==0:
        break
    cnt += K//c
    K %= c

print(cnt) 