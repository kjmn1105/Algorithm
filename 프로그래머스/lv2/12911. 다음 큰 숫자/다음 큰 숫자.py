def solution(n):
    # n을 2진수로 변환 > 1의 갯수 카운트
    one_cnt = str(bin(n)).count('1')
    
    m = n
    while True:
        m += 1
        if str(bin(m)).count('1') == one_cnt :
            return m    