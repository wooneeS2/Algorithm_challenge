
# #1075
# n = int(input())
# f = int(input())

# num = (n//100)*100

# i=0
# while True :
#     d = num%f    
#     if(d==0):
#         print(str(num)[-2:])
#         break
#     num+=1

    
#1076

color = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]

x = input()
y = input()
z = input()

print(((color.index(x)*10)+(color.index(y)))*(10**color.index(z)))
