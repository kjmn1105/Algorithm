import sys
input = sys.stdin.readline
N = int(input())
arr = []

for _ in range(N):
    num = int(input())
    # 0이 아닌 수가 입력되면 더하고
    if num :
        arr.append(num)
    # 0이 입력되면 마지막 수를 지운다
    else :
        arr.pop()

print(sum(arr))