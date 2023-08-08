N = int(input())
result = []

for i in range(1, N+1):
    result.append(" "*(N-i) + "*"*(2*i-1))

print("\n".join(result))
print("\n".join(reversed(result[:-1])))