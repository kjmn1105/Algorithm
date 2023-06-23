# [BOJ 1966] 프린터 큐
from collections import deque
케이스 = int(input())
for _ in range(케이스):
    _, target_idx = map(int, input().split())
    queue = deque(map(int, input().split()))
    cnt = 0

    while target_idx >= 0:
        # 맨 앞 숫자가 가장 높은 경우 빼준다. > 길이가 하나 줄어든 queue가 만들어진다.
        if queue[0] == max(queue):
            queue.popleft()
            target_idx -= 1
            cnt += 1

        # 아닐 경우 rotate 시킨다
        # target은 target_idx==0이면 맨 뒤로 이동, 0이 아닐 경우 한 칸 앞으로 이동
        else :
            queue.rotate(-1)
            target_idx += (-1 if target_idx else len(queue)-1)
    print(cnt)