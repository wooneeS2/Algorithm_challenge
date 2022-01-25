import sys


number = list(sys.stdin.readline())
nums=[]
number.pop()
for i in number:
    nums.append(int(i))


print(''.join(map(str,sorted(nums,reverse=True))))    
