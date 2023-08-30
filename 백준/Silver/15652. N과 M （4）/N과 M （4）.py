from itertools import combinations_with_replacement
N, M = map(int, input().split())

nums = list(combinations_with_replacement([i+1 for i in range(N)], M))
for i in nums:
    print(' '.join(map(str, i)))