import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Quicksort
        if not nums:
            return []
        if len(nums)==1:
            return nums
        pivot=random.choice(nums)
        less=[]
        equal=[]
        more=[]
        for num in nums:
            if num<pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                more.append(num)
        return self.sortArray(less)+equal+self.sortArray(more)
