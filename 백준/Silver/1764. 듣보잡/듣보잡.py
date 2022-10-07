import sys

a,b = map(int,sys.stdin.readline().split())

cant_hear_people = []
cant_watch_people=[]
total_people=[]

result = []

for _ in range(a):
        cant_hear_people.append(sys.stdin.readline().rstrip())

for _ in range(b):
        cant_watch_people.append(sys.stdin.readline().rstrip())
        
total_people = cant_watch_people+cant_hear_people

total_people.sort()
for i in range(len(total_people)):
        if total_people[i-1]==total_people[i]:
                result.append(total_people[i])

print(len(result))
for person in (result):
        print(person)

                
