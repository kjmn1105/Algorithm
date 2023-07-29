# [BOJ 1697번 숨바꼭질]
# BFS로 생각하기. 1개의 점 N에서 가능성은 N-1, N+1, N*2, 그 다음에는 선택지가 총 3*3가지
from collections import deque

def bfs(start, goal):
    max_limit = 10**5
    visited = [0 for _ in range(max_limit + 1)]
    queue = deque([start])

    while queue:
        # goal에 도착하면 종료 > visited에서 값 리턴
        curr = queue.popleft()
        if curr == goal:
            return visited[curr]

        # goal에 도착하지 않았고, 방문하지 않았으면 > visited에 +1 해서 저장 
        for n in (curr-1, curr+1, curr*2):
            if (0 <= n <= max_limit) and visited[n]==0 :
                visited[n] = visited[curr] + 1
                queue.append(n)

start, goal = map(int, input().split())
print(bfs(start, goal))