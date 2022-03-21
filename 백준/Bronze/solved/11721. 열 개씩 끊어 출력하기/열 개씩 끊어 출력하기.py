#11721
import sys
word = sys.stdin.readline()
word_list = list(word)

num = len(list(word))//10

for i in range(num+1):
    print("".join(word_list[0:10]))
    del word_list[0:10]
    
    