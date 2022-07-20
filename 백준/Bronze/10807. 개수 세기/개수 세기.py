import sys

count = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
number = int(sys.stdin.readline())

print(numbers.count(number))