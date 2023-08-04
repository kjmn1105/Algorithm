rule = [1, 1, 2, 2, 2, 8]
have = list(map(int, input().split()))

print(*[j-i for i, j in list(zip(have, rule))])