N = int(input())

# 몇번째 라인에 있는지 찾기
i = 1
while N > i*(i+1)/2:
    i += 1

# 라인에서 몇번쨰 순서인지 찾기
j = N - i*(i-1)//2

# i 홀짝에 따라 출력하기
print(f"{j}/{i-(j-1)}" if i%2==0 else f"{i-(j-1)}/{j}")