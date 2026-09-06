class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen=set()
        # for num in nums:
        #     if num not in seen:
        #         seen.add(num)
        #     else:
        #         return num that is the trivial solution with additional space

        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]

            if slow==fast:
                break
        slow=0
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]

        return slow