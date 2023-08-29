question = input()
words = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = []

for ch in question:
    for i, j in dict(enumerate(words)).items():
        if ch in j:
            result.append(i)

print(sum(map(lambda x: x+1, result)))