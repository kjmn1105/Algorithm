import sys
input = sys.stdin.readline

people = {}

for _ in range(int(input())):
    person, record = input().split()
    
    if person in people:
        people[person] += (1 if record=="enter" else -1)
    else:
        people[person] = 1

print("\n".join(sorted([person for person, record in people.items() if record==1], reverse=True)))