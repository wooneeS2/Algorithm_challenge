import sys

num_range = int(sys.stdin.readline())

num_list = []

num_list = list(map(int,sys.stdin.readline().split()))

target = int(sys.stdin.readline())

hashtable_dict = {}
count=0

for i in range (num_range):
    value = target - num_list[i]
    if hashtable_dict.get(value) is not None :
        count+=1
    hashtable_dict[num_list[i]] = i

print(count)

    