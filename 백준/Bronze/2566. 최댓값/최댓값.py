result = []
for i in range(9):
    temp = sorted(list(enumerate(list(map(int, input().split())))), key=lambda x: -x[1])
    result.append((i, temp[0][0], temp[0][1]))

max_val = sorted(result, key=lambda x: -x[-1])
print(max_val[0][-1])
print(max_val[0][0]+1, max_val[0][1]+1)