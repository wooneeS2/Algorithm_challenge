import sys

n = int(sys.stdin.readline())

sticks = []

result = 1

for i in range(n):
    sticks.append(int(sys.stdin.readline()))
#맨 마지막 기둥을 기준으로 세움
peek = sticks[-1]

# 기둥이 기준기둥보다 크다면 result+1 한 뒤, 기준 기둥을 큰 기둥으로 변경.
# 이렇게 해야 중복된 기둥들의 숫자가 카운트가 안 됨!  
for j in range(len(sticks)-1,-1,-1):
    if sticks[j] > peek:
        result +=1
        peek = sticks[j]

print(result)

