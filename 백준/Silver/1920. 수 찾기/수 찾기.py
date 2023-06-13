N = int(input())
A_list = set(map(int, input().split()))

M = int(input())
B_list = list(map(int, input().split()))

for b in B_list:
    print(int(b in A_list))