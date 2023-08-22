while True :
    a, b, c = sorted(map(int, input().split()))
    
    if (a, b, c) == (0, 0, 0):
        break
    
    if (c>=(a+b)) or (a<=0 or b<=0 or c<=0):
        print('Invalid')

    elif a==b==c:
        print('Equilateral')
    
    elif int(a==b) + int(b==c) + int(a==c) == 1:
        print('Isosceles')
    
    else :
        print('Scalene')
