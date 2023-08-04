N, M = map(int, input().split())
nums = [i+1 for i in range(N)]

for _ in range(M):
    i, j = map(lambda x: x-1, map(int, input().split()))
    nums = nums[:i] + nums[i:j+1][::-1] + nums[j+1:]

print(*nums)