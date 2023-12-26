for _ in range(int(input())):
    string = input()
    words = string.split(" ")
    reversed_words = [word[::-1] for word in words]
    print(" ".join(reversed_words))