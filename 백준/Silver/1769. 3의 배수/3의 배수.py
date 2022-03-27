#1769
import sys

def set_num(num):
    sum_nums = 0
    for i in num:
        sum_nums +=int(i)
    new_list = str(sum_nums).strip()
    return new_list

nums =list(map(int,sys.stdin.readline().strip()))
count=0

while True:    
    if len(nums)==1:
        print(count)
        if int(nums[0]) % 3 ==0 :
            print("YES")
            break
        else:
            print("NO")
            break
    else:
        nums = set_num(nums)
        count+=1

