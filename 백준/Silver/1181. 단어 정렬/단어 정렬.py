N = int(input())
words = list(set([input() for _ in range(N)]))
words = sorted(words)
words = sorted(words, key=lambda x: len(x))
print(*words)