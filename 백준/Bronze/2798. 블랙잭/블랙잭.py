from itertools import combinations

N, M = list(map(int, input().split()))
deck = list(map(int, input().split()))

# nC3 으로 3장씩 묶음 => 합이 M에 가장 가까운 경우 출력
cards = list(combinations(deck, 3))
print(max([sum(c) for c in cards if sum(c)<=M]))