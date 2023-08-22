a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print('Error')

elif a == b == c == 60:
    print('Equilateral')

elif int(a==b) + int(a==c) + int(b==c) == 1:
    print('Isosceles')

else:
    print('Scalene')