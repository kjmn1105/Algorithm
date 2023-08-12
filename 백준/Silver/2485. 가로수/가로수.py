import math
N = int(input())
nums = [int(input()) for _ in range(N)]
distance = [a-b for a, b in list(zip(nums[1:], nums[:-1]))]

gcd_num = math.gcd(*distance)
print(int(sum(map(lambda x: (x/gcd_num)-1, distance))))