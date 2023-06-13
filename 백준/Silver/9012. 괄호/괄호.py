N = int(input())
for _ in range(N):
    s = input()
    while '()' in s:
        s = s.replace('()', '')
    print('YES' if s=='' else 'NO')