import sys
input = sys.stdin.readline

def is_prime(n):
    """
    n의 소수 여부를 True, False로 리턴하는 함수
    """
    if n<2:
        return False
        
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

prime = [(1 if is_prime(i) else 0) for i in range(123456*2 + 1)]
while True:
    n = int(input())
    if n==0:
        break
    
    print(sum(prime[n+1:2*n+1]))