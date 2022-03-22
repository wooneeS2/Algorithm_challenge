import sys

num = int(sys.stdin.readline())
fibonacci = [0,1,1]
result = 0

if num<3 : result= fibonacci[num]
else :
    for i in range(3,num+1):
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    result = fibonacci[num]

print(result)


