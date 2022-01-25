#16446번

import sys


n = int(sys.stdin.readline())
#테스트케이스에 티켓번호 중복이 있어서 set으로 중복 없앤뒤 리스트 생성
sold_tickets = sorted(list(set(map(int,sys.stdin.readline().split()))))

#티켓의 가장 뒷 번호
max_ticket = max(sold_tickets)
#가장 뒷 번호를 기준으로 티켓 배열 생성
tickets = [n+1 for n in range(max_ticket)]


#티켓배열중에 팔린 티켓이 없으면 없는 부분 출력 
#티켓 배열만큼 모든 티켓이 팔렸으면 티켓 배열보다 하나 큰 티켓 출력
for i in range(max_ticket ):
    if sold_tickets[i] != tickets[i]:
        print(tickets[i])
        break
    elif sold_tickets == tickets:
        print(tickets[-1]+1)
        break
    



    
    
