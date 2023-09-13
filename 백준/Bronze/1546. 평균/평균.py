N = int(input())
nums = list(map(int, input().split()))[:N]

print(sum(nums)/len(nums) * 100/max(nums))