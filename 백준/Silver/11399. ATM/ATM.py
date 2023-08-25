N = int(input())
P = sorted(list(map(int, input().split())), reverse=True)

print(sum([(i+1)*j for i, j in list(enumerate(P))]))