# 입력횟수
T = int(input())

# H, W, guest를 받았을 때 호텔객실 배정
for _ in range(T):
    H, W, guest = list(map(int, input().split()))
    층 = (guest % H) or H
    호 = ((guest-1) // H) + 1
    print(층*100 + 호)