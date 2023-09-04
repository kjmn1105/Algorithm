m = int(input())
n1, n2, n3 = map(int, input())

print(f"""{m * n3}
{m * n2}
{m * n1}
{m*(n1*100 + n2*10 + n3)}""")