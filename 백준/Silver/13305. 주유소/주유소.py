import sys
input = sys.stdin.readline

N = int(input().rstrip())
dist = list(map(int, input().split()))[::-1]
price = list(map(int, input().split()))[-2::-1]
result = 0

while dist:
    curr_price = min(price)
    curr_idx = price.index(curr_price)

    result += sum(dist[:curr_idx+1]) * curr_price
    dist = dist[curr_idx+1:]
    price = price[curr_idx+1:]

print(result)