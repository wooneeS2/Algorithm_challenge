import sys
#알파벳 리스트를 만들어주는 모듈임포트
from string import ascii_lowercase

word = sys.stdin.readline()
alphabet = list(ascii_lowercase)
result = []

#js에서 indexOf역할을 하는 find
# 첫번째로 찾은 위치를 반환하고, 없으면 -1 리턴
for i in alphabet:
    result.append(word.find(i))
#리스트를 언팩킹하여 요구사항대로 출력    
print(*result)
