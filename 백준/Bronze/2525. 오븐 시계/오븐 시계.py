curr_h, curr_m = map(int, input().split())
cook_m = int(input())

h = (curr_h + (curr_m + cook_m)//60)%24
m = (curr_m + cook_m)%60

print(h, m)