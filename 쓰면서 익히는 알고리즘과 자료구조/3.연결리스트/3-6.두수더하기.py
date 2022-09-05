# 숫자의 각 자리 하나하나가 연결리스트로 표현되어있음
# 10이 넘어갈 경우 생기는 올림에 주의할 것

'''
1. 스택
- 스택 두개를 생성한다.
- 각 연결리스트를 각각 순회하면서 노드 값을 스택에 넣어주자
- 스택의 값을 하나씩 꺼내 자리수를 더해 나가도록 하자
- 더해진 각 값을 새로운 연결리스트의 노드로 연결해주자.

2. 연결 리스트 뒤집기
- 2개의 연결 리스트를 뒤집는다.
- 뒤집은 연결 리스트를 순회하며 각 자리수를 더한다. 
- 각 자리 숫자를 더하면서 새로운 노드를 생성하고 연결한다.

3. 문자열 연산
- 각 연력 리스트를 순회하면서 숫자를 문자열로 전환하고 문자열에 숫자를 추가함
- 두 문자열을 int로 변환
- 정수를 다시 str로 변환
- 각 자리를 접근하면서 연결 리스트 구성
'''
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#스택
def addTwoNumsByStack(l1,l2):
    st1=[]
    st2=[]
    
    l1_curr = l1
    l2_curr = l2
    
    head = None
    
    while l1_curr !=None:
        st1.append(l1_curr.val)
        l1_curr = l1_curr.next
    while l2_curr!=None:
        st2.append(l2_curr.val)
        l2= curr = l2_curr.next
    
    carry = 0
    
    while st1 or st2 :
        num1 = st1.pop() if st1 else 0
        num2 = st2.pop() if st2 else 0
        
        carry,num = divmod(num1+num2+carry,10)
        
        node = Node(num)
        if head == None :
            head = node
        else:
            temp = head
            head = node
            node.next = temp
    if carry != 0 :
        node = Node(carry)
        temp=head
        head = node
        node.next = temp
    
    return head
            

#연결 리스트 뒤집어서 더하기

def addTwoNumsByLinkedList(l1, l2):
    def reverse(head):
        prev = None
        curr = head
        
        while curr != None:
            next_temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = next_temp
        return prev
    
    r_l1 = reverse(l1)
    r_l2 = reverse(l2)
    
    res_head = None
    
    carry = 0
    
    while r_l1 != None or r_l2 != None:
        num1 = 0
        num2 = 0
        
        if r_l1!=None:
            num1 = r_l1.val
            r_l1 = r_l1.next
        if r_l2!=None:
            num2 = r_l2.val
            r_l2 = r_l2.next
        
        carry, num = divmod(num1+num2+carry,10)
        
        node = Node(num)
        if res_head == None:
            res_head = node
        else:
            temp = res_head
            res_head = node
            node.next = temp
    if carry != 0:
        node = Node(carry)
        temp = res_head
        res_head = node
        node.next = temp
    return res_head

def addTwoNumsByString(l1,l2):
    num1_str=''
    num2_str=''
    
    l1_curr = l1
    l2_curr = l2
    
    while l1_curr != None:
        num1_str = num1_str + str(l1_curr.val)
        l1_curr = l1_curr.next
    
    while l2_curr != None:
        num2_str = num2_str + str(l2_curr.val)
        l2_curr = l2_curr.next
        
    
    res_num = int(num1_str) + int(num2_str)
    
    #dummyNode
    head = Node(-1)
    curr = head
    for num_ch in str(res_num):
        curr.next = Node(int(num_ch))
        curr = curr.next
    
    curr.next = None
    return head.next