import sys

count = int(sys.stdin.readline())
numbers = list(sys.stdin.readline().rstrip())

sum = 0
for i in numbers:
    sum= sum+int(i)
print(sum)