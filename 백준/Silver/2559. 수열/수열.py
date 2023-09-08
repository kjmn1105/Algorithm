N, K = map(int, input().split())
nums = list(map(int, input().split()))
result = [sum(nums[:K])]

for i in range(N-K):
    result.append(result[i] - nums[i] + nums[i+K])

print(max(result))