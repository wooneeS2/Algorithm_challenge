import sys

input = sys.stdin.readline

N = int(input())
words=[]
for _ in range(N):
    words.append(input().strip())
set_result = set(words)
result = list(set_result)
result.sort()
result.sort(key=len)

for i in result:
    print(i)


        