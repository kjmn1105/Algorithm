# n, w, L : 트럭 개수, 다리 길이, 다리의 최대하중
n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

# 초기상태 (다리의 각 칸에 하중 0)
bridge = [0 for _ in range(w)]
time = 0

# 다리 위(bridge)에나 대기열(trucks)에 남아있지 않을 때까지 반복
while sum(bridge) + sum(trucks) > 0 :
    bridge.pop(0) # 다리 맨 앞은 통과
    if trucks and (sum(bridge) + trucks[0] <= L): # 최대하중 이하면,
        bridge += [trucks.pop(0)] # 대기열 맨 앞 트럭이 다리에 진입
    else :
        bridge += [0]
    time += 1

print(time)