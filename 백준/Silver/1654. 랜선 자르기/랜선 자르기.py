import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = [int(input().rstrip()) for _ in range(K)]

start, end = 1, max(arr)

while (start <= end):
    # 새로운 mid 에서의 랜선개수 cnt
    mid = (start + end)//2
    cnt = sum([i//mid for i in arr])

    if cnt >= N :
        start = mid + 1
    else :
        end = mid - 1

print(end)