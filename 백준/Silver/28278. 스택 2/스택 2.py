import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input().rstrip())):
    cmd = list(map(int, input().split()))

    if len(cmd)!=1:
        stack.append(cmd[1])
    elif cmd[0]==2:
        print(-1 if not stack else stack.pop())
    elif cmd[0]==3:
        print(len(stack))
    elif cmd[0]==4:
        print(1 if not stack else 0)
    elif cmd[0]==5:
        print(-1 if not stack else stack[-1])
