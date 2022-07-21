import sys


row,column = map(int,sys.stdin.readline().split())

list_a,list_b  = [],[]

for i in range(row):
    i = list(map(int,sys.stdin.readline().split()))
    list_a.append(i)

for i in range(row):
    i = list(map(int,sys.stdin.readline().split()))
    list_b.append(i)
    

for row in range(row):
    for col in range(column):
        print(list_a[row][col] + list_b[row][col], end=' ')
    print()