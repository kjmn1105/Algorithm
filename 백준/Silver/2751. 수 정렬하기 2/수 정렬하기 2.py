# 입출력이 최대 100만 개까지 필요하다 => 대량으로 처리 가능하도록
import sys
input = sys.stdin.readline

# 입력 > 정렬 > 출력
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

for i in sorted(nums):
    print(i)