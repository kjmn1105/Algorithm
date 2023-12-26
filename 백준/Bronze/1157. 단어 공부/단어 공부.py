from collections import Counter
counter = Counter(input().lower())
common = counter.most_common()

# 하나의 알파벳으로만 이루어진 단어를 주의해야 한다. (or RuntimeError)
print("?" if (len(common)>1 and common[0][1]==common[1][1]) else common[0][0].upper())