def solution(input_str):
    used_ch = []
    for ch in input_str:
        if (ch in used_ch) and (ch != used_ch[-1]):
            return 0
        else:
            used_ch.append(ch)
    return 1

result = 0
for _ in range(int(input())):
    result += solution(input())

print(result)