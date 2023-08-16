n = int(input())
coins = [25, 10, 5, 1]

for _ in range(n):
    total = int(input())
    result = []

    for c in coins:
        result.append(total//c)
        total %= c

    print(*result)