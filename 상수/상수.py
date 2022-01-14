import sys

numbers = sys.stdin.readline().split()

num = []
new_num=[]
temp_num=[]
for i in range(len(numbers)):
    temp = list(numbers[i].rstrip())
    num.append(temp)

for i in range(len(num)):
    for j in reversed(num[i]):
        temp_num.append(j)
    new_num.append(int("".join(temp_num)))
    temp_num=[]
    
print(max(new_num))