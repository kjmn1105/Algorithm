# [BOJ 9935] 문자열 폭발
string = input()
bomb = input()
stack = []

for ch in string:
    # string에 있는 글자를 하나씩 stack에 넣는다.
    stack.append(ch)

    # 넣은 글자가 bomb_fin과 같을 경우, bomb_len 길이만큼 이전에 stack에 넣은 글자도 확인한다.
    # bomb이 맞을 경우 제거한다.
    if (ch == bomb[-1]) and ("".join(stack[-len(bomb):])==bomb):
        for _ in range(len(bomb)):
            stack.pop()

remain = "".join(stack)
print(remain or "FRULA")