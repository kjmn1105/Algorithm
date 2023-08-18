import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    
    factors = [i for i in range(1, n) if n%i==0]
    
    if n != sum(factors):
        print(f"{n} is NOT perfect.")
    else:
        print(f'{n} = {" + ".join(map(str, factors))}')