#4673
num=10000
#1부터 10000까지의 배열 생성
numbers = [n+1 for n in range(num)]
self_numbers=[]

for i in numbers:
    self_number=0
    list_number = list(str(i))
    #숫자가 10보다 작을 경우 셀프 넘버는 두배가 됨
    if i//10 <1:
        self_number = i*2
    else :
        self_number = i
        #두자리 이상 숫자를 문자열로 쪼개서 리스트에 넣음
        for j in list_number:
            #문자열의 수를 int로 바꿔서 계속 더해서 셀프 넘버를 만듦
            self_number+=int(j)
    #만들어진 셀프 넘버를 배열에 추가함.
    self_numbers.append(self_number)    
#셀프 넘버들이 배열에 없으면 없는 숫자들 출력
for k in numbers:
    if k not in self_numbers:
        print(k)
