import sys

num = sys.stdin.readline()
if(num[1]=='0'):
    print(10+int(num[2:]))
else:
    print(int(num[0])+int(num[1:]))
    