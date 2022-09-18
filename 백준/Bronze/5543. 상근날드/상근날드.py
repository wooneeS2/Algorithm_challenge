
import sys

input = sys.stdin.readline

hamburgers=[]
beverages = []
for _ in range(3):
    hamburgers.append(int(input()))

for _ in range(2):
    beverages.append(int(input()))
    
print(min(hamburgers)+min(beverages)-50)
    
