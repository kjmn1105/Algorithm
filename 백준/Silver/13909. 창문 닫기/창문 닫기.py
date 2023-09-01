# 입력받은 수 n보다 작은 제곱수의 개수
n = int(input())

제곱수 = [i**2 for i in range(1, int(2100000000 **0.5)+1)]
print(len([i for i in 제곱수 if i<=n]))