# [BOJ 17298] 오큰수

N = int(input())
nums = list(map(int, input().split()))
answer = [-1] * N
stack = [0]

for i in range(N):
    while stack and nums[stack[-1]] < nums[i]:
        answer[stack.pop()] = nums[i]
    stack.append(i)

print(*answer)