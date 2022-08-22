import sys

a,b,v = map(int,sys.stdin.readline().split())


meter= (v-b) % (a-b)
days = (v-b) // (a-b)


if meter == 0 :
    print(days)
else :
    print(days+1)

# while(meter<=v):
#     days+=1
#     meter+=a
#     if meter==v:
#         break
#     meter-=b

# print(days)