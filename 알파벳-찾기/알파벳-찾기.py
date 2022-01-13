import sys
from string import ascii_lowercase

word = sys.stdin.readline()
alphabet = list(ascii_lowercase)
result = []

for i in alphabet:
    result.append(word.find(i))
    
print(*result)