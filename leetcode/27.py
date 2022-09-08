class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=len(nums)
        for i in range(len(nums)):
            if val in nums:
                count-=1
                del nums[nums.index(val)]
                nums.append('_')
                
        return count