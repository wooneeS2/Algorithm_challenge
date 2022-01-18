import sys 
count = int(sys.stdin.readline())
result = []

#테스트케이스 수 만큼 반복
for i in range(count):
    #조건을 배열로 받음
    condition = sys.stdin.readline().split()
    #문자열을 한글자씩 끊어서 리스트에 저장
    strings = list(condition[1].rstrip())
    #반복되는 숫자 저장
    repeat = int(condition[0])
    #문자열만큼 반복
    for j in strings:
        #문자하나*반복되는 수 곱한 문자를 리스트에 저장
       result.append(j*repeat) 
    #리스트에 저장된 반복된 문자열을 띄어쓰기 없이 출력
    print(''.join(result))
    #다음 테스트케이스를 위해 배열 초기화
    result=[]
