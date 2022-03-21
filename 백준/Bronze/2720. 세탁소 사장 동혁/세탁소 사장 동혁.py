#2720

import sys

count = int(sys.stdin.readline())
for _ in range(count):
    change= int(sys.stdin.readline())
    coins = [25,10,5,1]
    result =[]
    for coin in coins:
        result.append(change//coin)
        change = change%coin
    print(*result)
    

    

 