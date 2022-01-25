#4673
num=10000
numbers = [n+1 for n in range(num)]
self_numbers=[]

for i in numbers:
    self_number=0
    list_number = list(str(i))
    if i//10 <1:
        self_number = i*2
    else :
        self_number = i
        for j in list_number:
            self_number+=int(j)
    self_numbers.append(self_number)    

for k in numbers:
    if k not in self_numbers:
        print(k)
