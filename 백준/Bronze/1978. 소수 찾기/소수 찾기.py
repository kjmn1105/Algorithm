def prime_number(n):
    if n<2 :
        return False
    for i in range(2, (n//2) +1):
        if n%i == 0:
            return False
    return True

N = int(input())
num_list = list(map(int, input().split()))[:N]
print(sum([prime_number(num) for num in num_list]))