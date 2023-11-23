N = int(input()) # 타겟
M = int(input()) # S의 길이
S = input() # 문자열

# 'IO'를 'A'로 묶어준다.
new_S = S.replace('IO', 'A')

# 'A'뒤에 'I'가 오는 경우를 카운트 한다. 'O'가 나오면 카운트가 끊긴다.
new_S = new_S.replace('I', 'IO')
temp_list = new_S.split('O')
cnt_list = [(len(t)-N) for t in temp_list if len(t)>=N]

# 결과값 출력
print(int(sum(cnt_list)))