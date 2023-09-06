total = int(input())
result = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    result += a*b

print("Yes" if result==total else "No")