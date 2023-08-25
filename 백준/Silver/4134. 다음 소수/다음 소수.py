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

for _ in range(int(input())):
    n = int(input())
    while not is_prime(n):
        n+=1
    print(n)