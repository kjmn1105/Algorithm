import sys
input = sys.stdin.readline

N = int(input().rstrip())
gomgom = set()
cnt = 0

for _ in range(N):
    log = input().rstrip()

    if log == 'ENTER':
        gomgom.clear()

    elif log not in gomgom:
        gomgom.add(log)
        cnt += 1

print(cnt)