# 방법2 : max_len을 넣을 때마다 비교하기

import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
n = int(input())
result = (0, 0)

for _ in range(n):
    info = list(map(int, input().split()))
    if len(info)==2:
        queue.append(info[1])
    else:
        queue.popleft()

    if (len(queue) > result[0]) or (
        (len(queue)==result[0]) and (queue[-1] < result[1])):
        result = (len(queue), queue[-1])
        
print(*result)