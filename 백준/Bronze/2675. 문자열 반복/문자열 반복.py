for _ in range(int(input())):
    r, word = input().split()
    r = int(r)
    print(''.join([ch*r for ch in word]))