while True :
    a, b, c = sorted(list(map(int, input().split())))
    
    # 종료 조건
    if (a, b, c) == (0, 0, 0):
        break
    
    # 직각삼각형 조건
    cond1 = (a>0) and (b>0) and (c>0)
    cond2 = (a+b > c)
    cond3 = (a**2 + b**2 == c**2)
    print('right' if cond1 and cond2 and cond3 else 'wrong')