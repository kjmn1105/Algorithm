M = int(input())
N = int(input())

def is_prime(n):
    if n==2:
        return True

    elif n<2 or n%2==0:
        return False
    
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
    return True

nums = [i for i in range(M, N+1) if is_prime(i)]
if nums:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)