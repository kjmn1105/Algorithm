num = 0
while True:
    num += 1
    stack = []
    count = 0
    S = input()

    if "-" in S :
        break
    
    # {와 매치되면 지우고, 안되면 stack에 쌓아둔다.
    for ch in S :
        if ch == "{":
            stack.append(ch)
        else :
            if stack :
                stack.pop()
            else:
                count += 1
                stack.append("{")
                
    # stack에 같은 문자만 쌓여서 남아있을 경우  
    count += len(stack)//2
    
    print(f"{num}. {count}")