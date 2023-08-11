words = [input() for _ in range(5)]
result = ""
for j in range(max([len(w) for w in words])):
    for i in range(5):
        try:
            result += words[i][j]
        except:
            continue
            
print(result)