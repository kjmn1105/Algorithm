N = int(input())
cards = list(map(int, input().split()))
cards_dict = {c:1 for c in cards}

M = int(input())
checks = list(map(int, input().split()))

print(*[(1 if ch in cards_dict else 0) for ch in checks])