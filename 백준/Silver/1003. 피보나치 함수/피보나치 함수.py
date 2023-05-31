def solution(n):    
    zero = [1, 0, 1]
    one = [0, 1, 1]

    if len(zero) > n:
        return (zero[n], one[n])

    a, b = zero[-1], one[-1]
    for i in range(1, n-1):
        a, b = b, (a+b)

    return a, b

T = int(input())
for _ in range(T):
    a, b = solution(int(input()))
    print(f'{a} {b}')