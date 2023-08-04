from collections import deque

N = int(input())
queue = deque(map(int, input().split()))
stack = deque()
ord = 1

while queue:
    if queue[0]!=ord:
        stack.append(queue.popleft())

    else :
        queue.popleft()
        ord += 1

    while stack and stack[-1]==ord:
        stack.pop()
        ord += 1    

print("Nice" if not stack else "Sad")