from collections import deque
N = int(input())
balloon_list = [i+1 for i in range(N)]
cmd_list = list(map(int, input().split()))

queue = deque(zip(balloon_list, cmd_list))
result = []
while queue:
    balloon, cmd = queue.popleft()    
    result.append(balloon)
    queue.rotate(-(cmd-1) if cmd>=0 else -cmd)

print(*result)