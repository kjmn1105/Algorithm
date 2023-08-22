import sys
input = sys.stdin.readline

dancer = set(['ChongChong'])

N = int(input().rstrip())

for _ in range(N):
    users = set(input().split())
    if users.intersection(dancer):
        dancer.update(users)

print(len(dancer))