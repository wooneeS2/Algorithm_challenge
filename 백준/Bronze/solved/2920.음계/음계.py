import sys

scale = list(map(int,sys.stdin.readline().strip().split(" ")))

compare= [n for n in range(1,9) ]

if scale == compare:
    print("ascending")
    
elif scale == sorted(compare, reverse=True) :
    print("descending")
else : 
    print("mixed")