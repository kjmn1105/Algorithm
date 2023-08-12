import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
is_stack = list(map(int, input().split()))
nums = list(map(int, input().split()))

M = int(input())
C = list(map(int, input().split()))

# stack인 경우는 그냥 없애버린다.
queue = deque([b for a, b in list(zip(is_stack, nums)) if a==0])

result = []
for c in C:
    queue.appendleft(c)
    result.append(queue.pop())

print(*result)