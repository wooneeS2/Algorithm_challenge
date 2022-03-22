import sys

num = int(sys.stdin.readline())

def sugar_delivery(n):
    result = n
    for i in range(1,n//3+1):
        for j in range(1,n//3+1):
            if i*3 == n:
                if i<result:
                    result=i
            elif j*5 == n:
                if j<result:
                    result=j
            elif i*3 + j*5 ==n:
                if i+j<result:
                    result=i+j
    
    if result==n:
        return -1        
    return result

print(sugar_delivery(num))


