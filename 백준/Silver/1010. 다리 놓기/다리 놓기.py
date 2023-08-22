import math

T = int(input())
for _ in range(T):
    a, b = sorted(map(int, input().split()))
    print(math.comb(b, a))