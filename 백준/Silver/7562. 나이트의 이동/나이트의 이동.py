# [BOJ 7562번 나이트의 이동]
from collections import deque

def bfs(max_limit, start, goal):
    queue = deque([])
    queue.append(start)
    visited = [[0]*max_limit for _ in range(max_limit)]

    while queue:
        curr = queue.popleft()

        # goal에 도착할 경우
        if curr == goal:
            return visited[curr[1]][curr[0]]

        # goal에 도착하지 않았을 경우 > 다음 가능성들을 queue에 넣어준다.
        next = [(curr[0]+1, curr[1]+2), (curr[0]+1, curr[1]-2),
                (curr[0]-1, curr[1]+2), (curr[0]-1, curr[1]-2),
                (curr[0]+2, curr[1]+1), (curr[0]+2, curr[1]-1),
                (curr[0]-2, curr[1]+1), (curr[0]-2, curr[1]-1)]

        for i in next:
            if (0 <= i[0] < max_limit) and (0<= i[1] < max_limit):
                if visited[i[1]][i[0]] == 0:
                    visited[i[1]][i[0]] = visited[curr[1]][curr[0]] + 1
                    queue.append(i)

N = int(input())
for _ in range(N):
    min_limit, max_limit = 0, int(input())
    start = tuple(map(int, input().split()))
    goal = tuple(map(int, input().split()))

    print(bfs(max_limit, start, goal))