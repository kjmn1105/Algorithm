from itertools import product
N, M = map(int, input().split())

prd = list(product([i+1 for i in range(N)], repeat=M))
for i in prd :
    print(' '.join(map(str, i)))