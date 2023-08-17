while True:
    n, m = map(int, input().split())
    if (n, m) == (0, 0):
        break
    
    print("factor" if m%n==0 else ("multiple" if n%m==0 else "neither"))