from itertools import combinations
N, M = map(int, input().split())

temp_list = list(combinations([str(i) for i in range(1, N+1)], M))
for temp in temp_list:
    print(' '.join(temp))