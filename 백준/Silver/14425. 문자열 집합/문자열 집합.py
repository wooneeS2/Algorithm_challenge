import sys

a,b = map(int,sys.stdin.readline().split())

str_a = []
str_b=[]
count=0

for _ in range(a):
        str_a.append(sys.stdin.readline().rstrip())
for _ in range(b):
        str_b.append(sys.stdin.readline().rstrip())
        


for i in str_b:
        if i in str_a:
                count+=1

print(count)
                