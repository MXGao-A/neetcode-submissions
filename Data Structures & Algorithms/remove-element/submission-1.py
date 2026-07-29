class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert_index=0 
        for iter_index in range(len(nums)):
            if nums[iter_index]==val:
                continue
            elif nums[iter_index]!=val:
                nums[insert_index]=nums[iter_index]
                insert_index+=1
        return insert_index