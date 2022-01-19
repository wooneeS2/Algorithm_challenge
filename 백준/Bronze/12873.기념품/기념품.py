import sys
from collections import deque

n = int(sys.stdin.readline())
queue =deque([i for i in range(1,n+1) ])
t =1
pointer = 0
for i in range(n-1):
    number = (t**3) % len(queue)
    if t ==1 :
        queue.popleft()
    else :
        
        if number == 1:
            queue.popleft()
        else:    
            queue.rotate(-(number-1))            
            queue.popleft()
        
    t+=1
print(*queue)











    