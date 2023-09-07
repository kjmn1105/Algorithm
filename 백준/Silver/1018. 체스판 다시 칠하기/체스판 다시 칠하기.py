# 입력 > 원래 체스판 만들기
M, N = map(int, input().split())
board = []
for _ in range(M):
    board.append(list(input()))

# 기준점 정하기
count_list = []
for a in range((M-8)+1):
    for b in range((N-8)+1):
        # 기준 색 정하기
        color = board[a][b]
        count = 0

        # (a, b)에서 떨어진 칸수를 기준으로 > color==색, color!=색 카운트
        for i in range(8):
            for j in range(8):
                count += int(((i+j)%2==1) and (board[a+i][b+j] == color))
                count += int(((i+j)%2==0) and (board[a+i][b+j] != color))
        count_list.append(count)

# 기준색을 바꿔버리는 경우도 고려해서 최소값 찾기 > 출력
print(min(min(count_list), 64-max(count_list)))