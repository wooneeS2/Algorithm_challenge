#2609
import sys

numbers = list(map(int,sys.stdin.readline().split()))

least_multiple = []


if numbers[0]==numbers[1]:
    print(numbers[0])
    print(numbers[1])
    sys.exit()
for i in range(1,max(numbers)):
    if numbers[0]%i ==0 and numbers[1]%i==0:
        least_multiple.append(i)
        
if least_multiple :    
    print(max(least_multiple))  
    print(int((numbers[0]*numbers[1])/max(least_multiple)))




    