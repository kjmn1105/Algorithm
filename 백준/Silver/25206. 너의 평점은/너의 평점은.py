score_dict = {
    'A+':4.5, 
    'A0':4.0, 
    'B+':3.5, 
    'B0':3.0, 
    'C+':2.5, 
    'C0':2.0, 
    'D+':1.5, 
    'D0':1.0, 
    'F':0.0
    }
total, result = 0, 0

for _ in range(20):
    과목명, 학점, 성적 = input().split()

    if 성적 != 'P':
        학점 = float(학점)
        성적 = score_dict[성적]
        total += 학점
        result += 학점 * 성적

print('%.6f' % (result / total))