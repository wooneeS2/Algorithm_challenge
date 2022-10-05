import sys

for _ in range(3):
    nums = list(map(int,sys.stdin.readline().split()))

    if sum(nums)==3:
            print('A')
    if sum(nums)==2:
            print('B')
    if sum(nums)==1:
            print('C')
    if sum(nums)==4:
            print('E')
    if sum(nums)==0:
            print('D')


        