word = input()
subset = []
for i in range(1, len(word)+1):
    for j in range(len(word)-i+1):
        subset.append(word[j:j+i])

print(len(set(subset)))