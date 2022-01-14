import sys 
count = int(sys.stdin.readline())
result = []

for i in range(count):
    condition = sys.stdin.readline().split()
    strings = list(condition[1].rstrip())
    repeat = int(condition[0])
    for j in strings:
       result.append(j*repeat) 
       
    print(''.join(result))
    result=[]