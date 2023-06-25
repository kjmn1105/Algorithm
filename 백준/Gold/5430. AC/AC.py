# [BOJ 5430] AC
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cmd = input()
    n = int(input())
    queue = deque(eval(input()))
    R_cnt = 0

    try:
        for c in cmd:
            if c=="R":
                R_cnt+=1
            elif c=="D":
                queue.popleft() if R_cnt%2==0 else queue.pop()
        if R_cnt%2==1:
            queue.reverse()
        print("[" + ",".join(map(str, queue)) + "]")
    except:
        print("error")