def is_prime(n):
    if n==2:
        return True
    elif n<2 or n%2==0:
        return False

    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

N = int(input())
pf = [2] + [i for i in range(3, N+1, 2) if N%i==0 and is_prime(i)]

for f in pf:
    while N%f==0:
        print(f)
        N/=f