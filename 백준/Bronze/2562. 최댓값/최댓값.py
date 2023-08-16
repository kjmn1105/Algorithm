max = 0
max_idx = -1

for i in range(9):
    curr = int(input())
    
    if max <= curr:
        max = curr
        max_idx = i

print(max)
print(max_idx + 1)
