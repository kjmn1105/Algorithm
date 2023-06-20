import sys
input = sys.stdin.readline
coordinates = []

for _ in range(int(input())):
    coordinates.append(tuple(map(int, input().split())))

for c in sorted(coordinates, key=lambda x: (x[0], x[1])):
    print(f'{c[0]} {c[1]}')