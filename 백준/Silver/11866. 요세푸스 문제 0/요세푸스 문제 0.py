from collections import deque

N, k = map(int, input().split())
d = deque([i+1 for i in range(N)])

result = []
while d:
    d.rotate(-(k-1))
    result.append(str(d.popleft()))

print(f"<{', '.join(result)}>")