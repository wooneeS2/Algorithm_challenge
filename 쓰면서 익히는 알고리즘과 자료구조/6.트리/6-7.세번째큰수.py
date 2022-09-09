from audioop import reverse
import heapq
from tabnanny import check


def thirdMax(nums):
    cnt = 0
    third_max = 0
    
    check_dup = set()
    nums.sort(reverse=True)
    
    third_max = nums[0]
    
    for num in nums:
        if num in check_dup:
            continue
        check_dup.add(num)
        
        if cnt==2:
            third_max = num
            break
        
        cnt+=1
        
    return third_max

print(thirdMax([1,4,3,2,4,5,6,-2]))

def thirdMaxByQueue(nums):
    prio_queue = [item * -1 for item in list(dict.fromkeys(nums))]
    heapq.heapify(prio_queue)
    if len(prio_queue) > 2:
        cnt = 2
        
        while cnt>0:
            heapq.heappop(prio_queue)
            cnt-=1
            
    return prio_queue[0]*-1