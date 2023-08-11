background = [[0]*100 for _ in range(100)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    
    for i in range(x, x+10):
        for j in range(y, y+10):
            background[j][i] = 1

print(sum([sum(b) for b in background]))