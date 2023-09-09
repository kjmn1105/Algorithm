S = input()
q = int(input())

# 문자별 카운트 미리 만들어놓기 (dict)
cnt = {ch : [0] for ch in "abcdefghijklmnopqrstuvwxyz"}
for ch in cnt:
    for idx, s in enumerate(S):
        cnt[ch].append(cnt[ch][-1] + 1 if ch==s else cnt[ch][-1])

for _ in range(q):
    a, i, j = input().split()
    i, j = int(i), int(j)
    print(cnt[a][j+1] - cnt[a][i])