# [BOJ 1260번] DFS와 BFS
# 2023-07-08

from collections import deque

# N=정점개수, M=간선개수, V=탐색시작번호, graph=인접영행렬
N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]

# 방문한 곳, 방문한 순서 기록할 리스트
visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)
answer_dfs = []
answer_bfs = []

# 인접리스트 생성 : 간선을 입력받아서 => graph에 표시해준다.
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1
    # (1, 2)를 받으면 (2, 1)도 동일하게 길이 있다.


def dfs(V):
    """
    시작노드(V)를 받으면
    > 연결된 노드들을 순서대로 재귀적으로 반복 적용
    > 깊이우선탐색(dfs)를 수행하는 함수
    """
    # 현재노드 방문처리
    visited_dfs[V] = 1
    answer_dfs.append(V)

    # 현재노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(1, N+1):
        # graph에서 길이 있는데, visited_dfs에 방문기록이 없으면
        if((not visited_dfs[i]) and graph[V][i]):
            dfs(i)

dfs(V)
print(*answer_dfs)


def bfs(V):
    """
    시작노드(V)를 받으면
    > 연결된 노드들을 순서대로 재귀적으로 반복 적용
    > 너비우선탐색(bfs)를 수행하는 함수
    """
    # 방문해야할 곳을 순서대로 넣을 큐
    queue = deque()
    queue.append(V)
    visited_bfs[V] = 1

    while(queue):
        V = queue.popleft()
        answer_bfs.append(V)
        for i in range(1, N+1):
            if((not visited_bfs[i]) and graph[V][i]):
                queue.append(i)
                visited_bfs[i]=1


bfs(V)
print(*answer_bfs)