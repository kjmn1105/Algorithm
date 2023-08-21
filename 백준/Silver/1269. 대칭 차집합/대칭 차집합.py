N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A.union(B)) - len(A.intersection(B)))