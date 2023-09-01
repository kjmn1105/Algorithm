import sys
input = sys.stdin.readline

# prime : 에라토스테네스의 체 활용
prime = [False, False] + [True]*999999
for i in range(2, 100001):
    if prime[i]:
        for j in range(i*2, 1000001, i):
            prime[j] = False

# 골드바흐 파티션 
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    print(sum([1 for j in [2]+list(range(3, n//2+1, 2)) if prime[j] and prime[n-j]]))