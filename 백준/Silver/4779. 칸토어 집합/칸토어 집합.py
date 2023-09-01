import sys
input = sys.stdin.readline

def cantor(N):
    if N==0:
        return "-"
    return cantor(N-1) + (" " * 3**(N-1)) + cantor(N-1)

while True:
    try:
        N = int(input().rstrip())
        print(cantor(N))
    except:
        break