import sys
input = sys.stdin.readline

N, M = map(int, input().split())

포켓몬_dict = {}
for i in range(N):
    포켓몬 = input().rstrip()
    포켓몬_dict[str(i+1)] = 포켓몬
    포켓몬_dict[포켓몬] = i+1

for _ in range(M):
    print(포켓몬_dict[input().rstrip()])