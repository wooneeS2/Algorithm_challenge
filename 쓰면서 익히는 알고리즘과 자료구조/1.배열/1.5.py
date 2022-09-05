class Solution:
    def searchInsert(self, num_list: List[int], target: int) -> int:
        index = 0

        while index<len(num_list):
            if target <=num_list[index]:
                break
            index+=1

        return( index)