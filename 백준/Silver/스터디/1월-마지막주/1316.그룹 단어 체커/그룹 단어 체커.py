import sys

n = int(sys.stdin.readline())

result = 0

for i in range(n):
    #마지막 공백을 제거한 채로 리스트로 단어 받기
    word = list(sys.stdin.readline().rstrip())
    #단어가 그룹 단어인지 아닌지 값을 담는 변수
    word_check =False
    #글자가 하나씩만 있을 경우 그룹단어 체크
    if len(set(word)) == len(word) : 
        word_check=True
    else :
        # 뒷알파벳과 앞에 알파벳이 같을 경우 그룹단어
        for j in range(len(word)-1):
            if word[j]==word[j+1]:
                word_check=True
            # 앞에 알파벳이 뒤에 더 나올경우 그룹단어 아님
            elif word[j] in word[j+1:]:
                word_check=False
                #한번이라도 그룹단어가 아니면 반복문 종료
                break
    # 참일 경우만 카운트
    if word_check :
        result+=1
            
print(result) 