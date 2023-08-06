N, M = map(int, input().split())
듣도 = [input() for _ in range(N)]
보도 = [input() for _ in range(M)]

듣도보도 = (set(듣도) & set(보도))
print(len(듣도보도))
print('\n'.join(sorted(듣도보도)))