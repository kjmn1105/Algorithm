import sys
input = sys.stdin.readline

for i in range(int(input().rstrip())):
    a, b = input().split()
    print(f"Case #{i+1}: {a} + {b} = {int(a)+int(b)}")