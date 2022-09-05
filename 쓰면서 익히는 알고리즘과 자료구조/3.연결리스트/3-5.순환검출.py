#주어진 연결리스트가 순환을 가지는지  판단하는 프로그램짜기
# 순환이란? 특정 노드를 기점으로 이전 특정 노드로 돌아가 순환이 생기는 경우

'''
1. 전체 탐색 
- 노드를 순회한다.
    1. 순회 중 노드가 끝에 도달하거나 연결이 없다면 종료
    2. 현재까지 순회 카운터를 기록
    3. 노드를 처음부터 순회 카운터만큼 순회한다.
        - 바깥 순회에서 선택된 노드와 비교해 2번 겹친다면 순환 발생
        - 아니라면 순환 종료

2. 해시테이블
- 노드를 순회한다.
    1. 각 노드를 set으로 있는지 없는지 확인
    2. 있다면 true 반환
    3. 없으면 set에 추가

3. 투 포인터
- slow, fast포인터는 head를 가르킨다.
- slow는 1번 이동한다.
- fast는 2번 이동한다.
- fast와 slow가 같아진다면 연결 리스트는 순환임.
- fast와 slow가 가리키는 노드가 None이면 순환이 없음.
    
'''



class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#투포인터로 순환 찾기
def hasCycleByTwoPointer(self,head):
    outer = head
    
    node_cnt = 0
    
    while(outer != None and outer.next != None):
        outer =outer.next
        node_cnt +=1
        
        visit = node_cnt
        inner = head
        
        matched = 0
        
        while visit > 0 :
            if outer != inner :
                inner = inner.next
            if outer == inner :
                matched +=1
            if matched == 2:
                return True
            visit -=1
            
        return False
                
def hasCycleBySet(self,head):
    curr = head
    node_set = set()
    
    while curr != None:
        if curr in node_set:
            return True
        
        node_set.add(curr)
        curr = curr.next
        
    return False

def hasCycleBySlowFast(self,head):
    slow = head
    fast = head
    
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False