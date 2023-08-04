import sys
input = sys.stdin.readline

정원 = [i for i in range(1, 31)]
submission = [int(input()) for _ in range(28)]

for i in sorted(set(정원) - set(submission)):
    print(i)