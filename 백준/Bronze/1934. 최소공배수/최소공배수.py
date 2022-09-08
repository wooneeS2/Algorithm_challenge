import sys

# def lcm(a,b):
#      for i in range(max(a,b),(a*b)+1):
#             if i%a==0 and i%b==0:
#                 return i

# N = int(sys.stdin.readline())
# for _ in range(N):
#     A,B = map(int,sys.stdin.readline().split())
#     print(lcm(A,B))
            
            
N = int(sys.stdin.readline())

for i in range(N):
    a,b = map(int,sys.stdin.readline().split())
    x,y = max(a,b),min(a,b)
    while y:
        x,y = y,x%y
    print(a*b//x)