from collections import deque
import sys
input = sys.stdin.readline

d = deque()
for _ in range(int(input())):
    cmd = list(map(int, input().split()))

    if cmd[0]==1:
        d.appendleft(cmd[1])
    elif cmd[0]==2:
        d.append(cmd[1])
    elif cmd[0]==3:
        print(-1 if not d else d.popleft())
    elif cmd[0]==4:
        print(-1 if not d else d.pop())
    elif cmd[0]==5:
        print(len(d))
    elif cmd[0]==6:
        print(1 if not d else 0)
    elif cmd[0]==7:
        print(-1 if not d else d[0])
    elif cmd[0]==8:
        print(-1 if not d else d[-1])