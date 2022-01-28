#2751번

import sys 

n = int(sys.stdin.readline())
numbers=[]

for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

for i in sorted(numbers):
    print(i)