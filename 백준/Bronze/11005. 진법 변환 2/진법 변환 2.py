N, B = map(int, input().split())
alph_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = []

while N >= B :
    result.append(N%B)
    N //= B
result.append(N)

result = result[::-1]
result = list(map(lambda x: dict(enumerate(alph_list))[x], result))
print(''.join(result))