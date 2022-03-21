#10162

import sys

m = int(sys.stdin.readline())

buttons = [300,60,10]
result = []
for button in buttons :
    if m%10 !=0:
        print(-1)
        break 
    result.append(m//button)
    m = m%button
    

print(*result)