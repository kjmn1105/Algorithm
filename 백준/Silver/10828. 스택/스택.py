import sys
input = sys.stdin.readline
N = int(input())

stack = []
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        try :
            print(stack.pop())
        except :
            print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(int(len(stack)==0))
    elif cmd[0] == 'top':
        try :
            print(stack[-1])
        except :
            print(-1)