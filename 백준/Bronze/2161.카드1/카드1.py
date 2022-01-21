#2161번

import sys
from collections import deque

n = int(sys.stdin.readline())

numbers = deque([i+1 for i in range(n)])
result = []

for i in range(n):
    result.append(numbers[0])
    numbers.popleft()
    numbers.rotate(-1)

print(*result)
    
