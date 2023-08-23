from collections import Counter
import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = sorted([int(input().rstrip()) for _ in range(N)])

# mean
print(int(round(sum(nums)/N)))

# median
print(nums[N//2])

# most_frequent
if N==1:
    print(nums[0])
else:
    a, b = Counter(nums).most_common()[:2]
    print(b[0] if a[1]==b[1] else a[0])

# range
print(nums[-1] - nums[0])