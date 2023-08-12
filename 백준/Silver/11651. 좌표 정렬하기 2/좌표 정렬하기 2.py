N = int(input())
coordinates = []

for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

for x, y in sorted(coordinates, key=lambda x: (x[1], x[0])):
    print(x, y)