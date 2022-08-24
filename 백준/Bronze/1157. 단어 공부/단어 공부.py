import sys

word = list(sys.stdin.readline().rstrip().upper())

wordMap={}
for i in range(len(word)):
    if wordMap.get(word[i]) != None:
        wordMap[word[i]] = wordMap.get(word[i])+1
    else:
        wordMap[word[i]] = 1
    

result = [k for k,v in wordMap.items() if max(wordMap.values()) == v]


if len(word)<=1:
    print(*word)
elif len(result) >1 :
    print('?')
else:
    print(*result)
    
    