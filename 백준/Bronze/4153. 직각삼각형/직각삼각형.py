import sys

input = sys.stdin.readline


while True :
    tri = list(map(int,input().split()))
    if sum(tri)==0:
        break
    max_len = max(tri)
    min_len = min(tri)
    tri.remove(max_len)
    tri.remove(min_len)
    middle = tri[0]
    
    if (middle**2+min_len**2)==max_len**2:
        print('right')
    else:
        print('wrong')
    




        