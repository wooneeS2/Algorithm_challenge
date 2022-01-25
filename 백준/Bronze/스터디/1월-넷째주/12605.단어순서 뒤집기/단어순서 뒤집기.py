import sys 

n = int(sys.stdin.readline())

result = []

for i in range(n):
    s = sys.stdin.readline().strip().split(' ')
    for j in range(len(s)-1,-1,-1):
        result.append(s[j])
    print("Case #%d:"%(i+1),*result)
    
    result =[]