# 기준보다 작은 수 중에 가장 오른쪽에 있는 것까지의 거리?

from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        cnt = 0
        curr = queue.popleft()
        
        for p in queue:
            cnt += 1
            if curr > p:
                break
        
        answer.append(cnt)
    return answer