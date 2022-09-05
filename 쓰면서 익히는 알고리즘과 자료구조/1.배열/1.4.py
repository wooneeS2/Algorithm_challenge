import sys

num_list = list(map(int,sys.stdin.readline().split()))

if len(num_list) <= 0:
    print(0) 

curr = num_list[0]
count=1

for i in range(1,len(num_list)):
    if curr!=num_list[i]:
        curr = num_list[i]
        num_list[count] = curr
        count+=1
print(count)