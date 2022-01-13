import sys

count = int(sys.stdin.readline())
#rstrip()으로 뒤에 오는 공백 및 엔터 제거
numbers = list(sys.stdin.readline().rstrip())
#문자열을 리스트에 넣어주면 그 자체로 한글자씩 리스트가 생성됨

sum = 0
for i in numbers:
    #문자열의 string을 int로 바꿔줌
    sum= sum+int(i)
print(sum)
