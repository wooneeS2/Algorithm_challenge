import sys
range_num = int(sys.stdin.readline())


coordinate_list=[]
for _ in range(range_num):
        [x,y] = map(int,sys.stdin.readline().split())
        coordinate_list.append([x,y])


result_list = sorted(coordinate_list)

for i in range(range_num):
        print(result_list[i][0], result_list[i][1])
        
