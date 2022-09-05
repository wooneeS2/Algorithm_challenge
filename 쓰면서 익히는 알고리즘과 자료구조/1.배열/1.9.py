
import sys

nums=[1,2,2,2,2,2,2,4,87]
def majority (nums) :
    majority_count = int(len(nums)/2)

    hashmap={}

    for num in nums:
        if hashmap.get(num) !=None:
            hashmap[num] = hashmap[num]+1
        else:
            hashmap[num] =1
        if hashmap[num] > majority_count:
            return(num)
            
    return(-1)

    
print(majority(nums))
    