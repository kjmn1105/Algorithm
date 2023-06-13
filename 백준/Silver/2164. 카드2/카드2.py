import math

N = int(input())
log2_N = math.log2(N)
print(N if log2_N==int(log2_N) else 2*(N-(2**int(log2_N))))