N, k = map(int, input().split())
nums = map(int, input().split())

print(sorted(nums, reverse=True)[k-1])