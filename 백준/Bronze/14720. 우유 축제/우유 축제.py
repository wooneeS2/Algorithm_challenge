#14720

import sys

store_count = int(sys.stdin.readline())
store_list = list(map(int,sys.stdin.readline().split()) )
count=0

for i in range(store_count):
    j = count%3
    if store_list[i] == j:
        count+=1
print(count)