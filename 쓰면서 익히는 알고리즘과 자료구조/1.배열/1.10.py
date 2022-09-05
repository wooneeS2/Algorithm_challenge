
nums = [0,3,1,5,6,2]
def findMissingNum (nums) :
    nums.sort()
    
    if nums[-1] != len(nums):
        return len(nums)
    if nums[0] !=0:
        return 0
    for i in range(1,len(nums)):
        if nums[i-1]+1 != nums[i]:
            return nums[i-1]+1
    return -1


print(findMissingNum(nums))