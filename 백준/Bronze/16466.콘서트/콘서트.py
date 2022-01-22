#16446번

import sys


n = int(sys.stdin.readline())

sold_tickets = sorted(list(set(map(int,sys.stdin.readline().split()))))


max_ticket = max(sold_tickets)

tickets = [n+1 for n in range(max_ticket)]



for i in range(max_ticket ):
    if sold_tickets[i] != tickets[i]:
        print(tickets[i])
        break
    elif sold_tickets == tickets:
        print(tickets[-1]+1)
        break
    



    
    
