# 11:42~

import collections
def solution(priorities, location):
    q = collections.deque(priorities)
    원래길이 = len(priorities)
    
    while len(q)>=location:
        if location==0 and q[0]==max(q):
            q.popleft()
            return 원래길이 - len(q)
            
        else:
            if q[0]==max(q):
                q.popleft()
                location -= 1
            else:
                q.rotate(-1)
                location -=1
            
        if location <0:
            location += len(q)