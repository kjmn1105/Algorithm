N, X = map(int, input().split())
nums = map(int, input().split())
print(*[n for n in nums if n < X])