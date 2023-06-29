def solution(s):
    stack = []
    
    for ch in s:
        if stack and ch==")" and stack[-1]=="(":
            stack.pop()
        else :
            stack.append(ch)
    return not bool(stack)
        
        