# [BOG 2178] 미로 탐색

from collections import deque

세로, 가로 = map(int, input().split())
graph = [list(map(int, input())) for _ in range(세로)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 방문하지 않은 곳은 0, 1로만 되어 있기 때문에 별도로 visited를 만들 필요가 없음.


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for dx, dy in d:
            x_, y_ = (x + dx), (y + dy)

            if (0<=x_<가로) and (0<=y_<세로) and graph[y_][x_]==1:
                graph[y_][x_] = graph[y][x] + 1
                queue.append((x_, y_))
            else : 
                continue

    return graph[세로-1][가로-1]

print(bfs(0, 0))