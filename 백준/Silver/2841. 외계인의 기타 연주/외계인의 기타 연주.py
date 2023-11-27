import sys
input = sys.stdin.readline

N, P = map(int, input().split())
temp = [[] for _ in range(N+1)]
cnt = 0

for _ in range(N):
    l, p = map(int, input().split())

    # p보다 크면 손가락은 뗀다.
    while temp[l] and (temp[l][-1] > p):
        temp[l].pop()
        cnt += 1

    if temp[l] and temp[l][-1]==p:
        pass

    # p보다 작거나 비어있으면, 손가락을 추가한다.
    else :
        temp[l].append(p)
        cnt += 1

print(cnt)