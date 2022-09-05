import sys
input = sys.stdin.readline()

num_list1 = list(map,int(input().split()))
m = int(input())
num_list2 = list(map,int(input().split()))
n = int(input())

for i, num_list1_item in enumerate(num_list1):
    if num_list1_item > num_list2[0]:
        num_list1[i] = num_list2[0]
        num_list2[0] = num_list1_item
        
        for k,item in enumerate(num_list2[1:],start=1):
            if num_list1_item <= item :
                num_list2[k-1] = num_list1_item
                break
            
            num_list2[k-1] = num_list2[k]

print(num_list1)