import sys
card_range = int(sys.stdin.readline())
card_list =set(map(int,sys.stdin.readline().split()))
number_range = int(sys.stdin.readline())
number_list = list(map(int,sys.stdin.readline().split()))
       
result_list=[] 
for i in range(len(number_list)):
        if(number_list[i] in card_list):
                result_list.append(1)
        else:
                result_list.append(0)
print(*result_list)

                
                







