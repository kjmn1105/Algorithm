from collections import deque

# 주어진 정보로 graph, visited 만들기
세로, 가로, K = map(int, input().split())
graph = [[0] * 가로 for _ in range(세로)]
visited = [[False] * 가로 for _ in range(세로)]
for _ in range(K):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1
d = [(0, -1), (0, 1), (1, 0), (-1, 0)]

# bfs 함수
def bfs(x, y):
    cnt = 0
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in d:
            x_, y_ = (x+dx), (y+dy)
            if (0<=x_<가로) and (0<=y_<세로):
                if graph[y_][x_]==1 and not visited[y_][x_]:
                    visited[y_][x_] = True
                    queue.append((x_, y_))
                    cnt += 1
            else:
                continue
    return cnt + 1

# 주어진 graph에서 bfs로 뭉쳐있는 쓰레기 찾기
answer = 0
for j in range(세로):
    for i in range(가로):
        if graph[j][i]==1 and not visited[j][i]:
            answer = max(answer, bfs(i, j))
print(answer)