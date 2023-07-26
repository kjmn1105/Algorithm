from collections import deque

가로, 세로 = map(int, input().split())
graph = [list(input()) for _ in range(세로)]
visited = [[False]*가로 for _ in range(세로)]
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# BFS 함수
def bfs(x, y, color):
    cnt = 0
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in d:
            x_, y_ = (x+dx), (y+dy)

            if (0<=x_<가로) and (0<=y_<세로) and (not visited[y_][x_]) and (graph[y_][x_]==color):
                visited[y_][x_] = True
                queue.append((x_, y_))
                cnt += 1
    return cnt + 1

# 묶음 카운트
W, B = 0, 0
for i in range(가로):
    for j in range(세로):
        if not visited[j][i]:
            W += bfs(i, j, 'W') ** 2 if graph[j][i]=='W' else 0
            B += bfs(i, j, 'B') ** 2 if graph[j][i]=='B' else 0
print(W, B)