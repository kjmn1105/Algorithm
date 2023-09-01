a=0
b=1
i=1

N = int(input())

while i<N+1:
    i+=1
    a, b = b, a+b

print(a)