a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

print(1 if (a1*n + a0 <= c*n) and (a1 <= c*n) else 0)