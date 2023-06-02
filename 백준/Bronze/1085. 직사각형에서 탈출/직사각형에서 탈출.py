x, y, w, h = list(map(int, input().split()))

result = min([abs(w-x), abs(x), abs(h-y), abs(y)])
print(result)