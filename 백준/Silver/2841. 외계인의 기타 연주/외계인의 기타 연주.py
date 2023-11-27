import sys
input = sys.stdin.readline

N, P = map(int, input().split())
temp = [[] for _ in range(N+1)]
cnt = 0

for _ in range(N):
    l, p = map(int, input().split())

    # l번 줄에서 p번 프렛보다 큰 곳은 다 손가락을 뗀다.
    while temp[l] and (temp[l][-1] > p):
        temp[l].pop()
        cnt += 1

    # l번 줄이 비어있거나 가장 큰 수의 프렛이 p보다 작으면 손가락을 추가한다.
    if (not temp[l]) or temp[l][-1] < p:
        temp[l].append(p)
        cnt += 1

print(cnt)