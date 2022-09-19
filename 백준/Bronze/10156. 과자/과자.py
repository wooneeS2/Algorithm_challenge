
import sys

input = sys.stdin.readline

price,count,now_money = map(int,input().split(' '))

if (price*count)-now_money <0 :
    print(0)
else:
    print((price*count)-now_money)
    
