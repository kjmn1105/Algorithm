N, B = input().split()
B = int(B)
alph_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0

for i, j in list(enumerate(N[::-1])):
    result += (B**i) * alph_list.index(j)

print(result)