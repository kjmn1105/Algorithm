import sys
import math
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    print(math.lcm(*map(int, input().split())))