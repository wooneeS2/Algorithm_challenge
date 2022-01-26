import sys

n = int(sys.stdin.readline())

result = 0

for i in range(n):
    word = list(sys.stdin.readline().rstrip())
    word_check =False
    if len(set(word)) == len(word) : 
        word_check=True
    else :
        for j in range(len(word)-1):
            if word[j]==word[j+1]:
                word_check=True
            
            elif word[j] in word[j+1:]:
                word_check=False
                break
    if word_check :
        result+=1
            
print(result) 