N = int(input())

i=0
while True :
    if N <= 3*i*(i+1) + 1:
        break
    i+=1
print(i+1)