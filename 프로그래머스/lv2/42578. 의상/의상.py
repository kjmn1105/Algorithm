import collections

def solution(clothes):
    clothes_count = collections.Counter([key for value, key in clothes])
    result = 1
    for k in clothes_count.values():
        result *= (k+1)
    return result-1
        
# (2C1 + 1) * (1C1 + 1) - 1 = 5
# (3C1 + 1) - 1 = 3
