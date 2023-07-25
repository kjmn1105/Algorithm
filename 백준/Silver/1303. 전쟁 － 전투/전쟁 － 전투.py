from collections import deque

N, M = map(int, input().split())
graph = [list(input()) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
move = ((-1, 0), (1, 0), (0, -1), (0, 1))
W_cnt, B_cnt = 0, 0


def dfs(x, y, color):
    global cnt

    if 0<=x<M and 0<=y<N and visited[x][y]==0 and graph[x][y]==color:
        visited[x][y] = 1
        cnt += 1
        for m in move:
            dfs(x+m[0], y+m[1], color)
        return True
    return False

result_W = 0
result_B = 0

for i in range(M):
    for j in range(N):
        cnt = 0
        if not visited[i][j] and dfs(i, j, 'W'):
            result_W += cnt ** 2
        
        cnt = 0
        if not visited[i][j] and dfs(i, j, 'B'):
            result_B += cnt ** 2

print(result_W, result_B)