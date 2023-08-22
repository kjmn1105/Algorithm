from collections import Counter
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

x = Counter([x1, x2, x3]).most_common()[-1][0]
y = Counter([y1, y2, y3]).most_common()[-1][0]
print(x, y)