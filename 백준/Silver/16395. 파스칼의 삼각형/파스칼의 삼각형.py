import sys

numRow, num = map(int,sys.stdin.readline().split())



pascal =[]

if numRow <= 0:
    print(pascal)

pascal.append([1])

for i in range(1, numRow):
    prev_len = len(pascal[i-1])
    curr_list = []
    
    for j in range(prev_len +1):
        nums =1
        if j!=0 and j!=prev_len:
            nums = pascal[i-1][j-1] + pascal[i-1][j]
        curr_list.append(nums)
            
    pascal.append(curr_list)

print(pascal[numRow-1][num-1])


    
    