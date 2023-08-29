word = input()
alph = 'abcdefghijklmnopqrstuvwxyz'
print(' '.join(map(str, [word.index(ch) if ch in word else -1 for ch in alph])))