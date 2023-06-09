while True:
    n = int(input())

    if n==0:
        break
    
    print('yes' if n == int(str(n)[::-1]) else 'no')