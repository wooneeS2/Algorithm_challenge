import sys

n = int(sys.stdin.readline())

sticks = []

result = 1

for i in range(n):
    sticks.append(int(sys.stdin.readline()))
    
peek = sticks[-1]
    
for j in range(len(sticks)-1,-1,-1):
    if sticks[j] > peek:
        result +=1
        peek = sticks[j]

print(result)

