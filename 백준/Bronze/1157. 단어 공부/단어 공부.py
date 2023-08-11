from collections import Counter
counter = Counter(input().lower())
common = counter.most_common()
print("?" if (len(common)>1 and common[0][1]==common[1][1]) else common[0][0].upper())