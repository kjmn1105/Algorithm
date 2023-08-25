import math
import sys
input = sys.stdin.readline
A_numer, A_denom = map(int, input().split())
B_numer, B_denom = map(int, input().split())

result = [(A_numer*B_denom + A_denom*B_numer), (A_denom*B_denom)]
gcd = math.gcd(*result)
print(*map(lambda x: int(x/gcd), result))