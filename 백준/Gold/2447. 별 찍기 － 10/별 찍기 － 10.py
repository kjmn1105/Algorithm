def draw_starts(n):
    if n==1:
        return ['*']
    
    module = draw_starts(n//3)
    L=[]

    for m in module:
        L.append(m*3)
    for m in module:
        L.append(m + ' '*(n//3) + m)
    for m in module:
        L.append(m*3)
    return L

print('\n'.join(draw_starts(int(input()))))