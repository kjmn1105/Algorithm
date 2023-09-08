import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [0]

for i, j in list(enumerate(nums)):
    prefix_sum.append((prefix_sum[-1] + j))

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])