A_row, A_col = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(A_row)]

B_row, B_col = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(B_row)]

result = [[0]*B_col for _ in range(A_row)]
for i in range(A_row):
    for k in range(B_col):
        result[i][k] = sum([A[i][j] * B[j][k] for j in range(A_col)])

for r in result:
    print(*r)