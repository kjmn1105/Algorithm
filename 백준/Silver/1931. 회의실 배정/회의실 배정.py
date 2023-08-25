import sys
input = sys.stdin.readline

N = int(input())
meeting = [tuple(map(int, input().split())) for _ in range(N)]
meeting = sorted(meeting, key=lambda x: (x[1], x[0]))
curr = 0
cnt = 0

for m in meeting:
    if m[0] >= curr:
        curr = m[1]
        cnt += 1

print(cnt)