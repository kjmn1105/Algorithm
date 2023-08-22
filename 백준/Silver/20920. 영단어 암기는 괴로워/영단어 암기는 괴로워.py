import sys
from collections import Counter
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
words = []

for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        words.append(word)

word_dict = sorted(list(Counter(words).items()), key=lambda x:(-x[1], -len(x[0]), x[0]))
for i, j in word_dict:
    print(i + '\n')