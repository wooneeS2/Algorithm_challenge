#2161번

import sys
from collections import deque

n = int(sys.stdin.readline())

#1부터 n까지 n개의 카드 생성
numbers = deque([i+1 for i in range(n)])

#버려지는 카드들
result = []

for i in range(n):
    #맨위의 카드 버려지는 항목에 추가
    result.append(numbers[0])
    #맨 위에 있는 카드 버리기
    numbers.popleft()
    #버린 다음 맨 위에 있는 카드 맨 밑으로 보내기
    numbers.rotate(-1)

print(*result)
    
