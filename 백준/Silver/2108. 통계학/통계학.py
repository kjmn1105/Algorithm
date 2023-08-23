from collections import Counter
import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = sorted([int(input().rstrip()) for _ in range(N)])

if N==1:
    print(nums[0])
    print(nums[0])
    print(nums[0])
    print(0)

else :
    print(int(round(sum(nums)/N)))
    print(nums[N//2])
    a, b = Counter(nums).most_common()[:2]
    print(b[0] if a[1]==b[1] else a[0])
    print(nums[-1] - nums[0])