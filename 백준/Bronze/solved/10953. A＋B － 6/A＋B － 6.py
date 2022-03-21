#10953
import sys

count = int(sys.stdin.readline())

for i in range(count):
    nums = map(int,sys.stdin.readline().split(","))
    print(sum(nums))