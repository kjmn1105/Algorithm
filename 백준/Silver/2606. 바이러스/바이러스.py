from collections import deque
nodes = int(input())
edges = int(input())
graph = [[0 for _ in range(nodes+1)] for _ in range(nodes+1)]
for _ in range(edges):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

infected = []
queue = deque()
queue.append(1)

while queue:
    x = queue.popleft()
    infected.append(x)
    queue.extend([idx for idx, value in enumerate(graph[x]) 
        if (value==1 and (idx not in infected) and (idx not in queue))])

print(len(infected) - 1)