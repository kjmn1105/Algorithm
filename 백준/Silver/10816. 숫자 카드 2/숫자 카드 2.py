import collections
import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))[:N]
nums_cnt = collections.Counter(nums)

M = int(input())
new_nums = list(map(int, input().split()))[:M]
for n in new_nums:
    print(nums_cnt[n], end=' ')