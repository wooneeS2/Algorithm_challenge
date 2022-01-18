import sys

numbers = sys.stdin.readline().split()

num = []
new_num=[]
temp_num=[]

#두 개의 숫자를 각각 따로 문자열로 바꿔서 배열로 저장해줌
for i in range(len(numbers)):
    temp = list(numbers[i].rstrip())
    num.append(temp)
    
#배열의 길이 만큼 반복
for i in range(len(num)):
    #배열을 거꾸로해서 temp_num에 저장
    for j in reversed(num[i]):
        temp_num.append(j)
    #new_num에 거꾸로된 숫자 배열을 문자열->int형으로 바꿔서 저장
    new_num.append(int("".join(temp_num)))
    temp_num=[]
#new_num에서 큰 숫자 출력    
print(max(new_num))
