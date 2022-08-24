import sys

best_scroe = 0
best_person=0

for i in range(5):
    score = list(map(int,sys.stdin.readline().split()))
    if best_scroe < sum(score):
        best_scroe = sum(score)
        best_person = i+1
        
print(best_person, best_scroe)
    