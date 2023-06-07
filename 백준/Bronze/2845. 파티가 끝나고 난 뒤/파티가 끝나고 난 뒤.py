import sys
party = list(map(int,sys.stdin.readline().split(' ')))
people = list(map(int,sys.stdin.readline().split(' ')))

party_people = party[0]*party[1]

result = []

for area in people:
        result.append(area-party_people)
        
print(*result)