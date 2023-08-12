N = int(input())
nums = list(map(int, input().split()))
cnt = sorted(set(nums), reverse=True)
cnt_dict = {cnt[i]: (len(cnt)-i-1) for i in range(len(cnt))}

print(*[cnt_dict[n] for n in nums])