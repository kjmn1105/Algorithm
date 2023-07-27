h, m = map(int, input().split())

if m-45>=0:
    new_h = h
    new_m = m - 45
else:
    new_m = 60 + m - 45
    new_h = 23 if h==0 else h-1

print(new_h, new_m)