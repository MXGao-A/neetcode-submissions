class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def subproblem(num_slice):
            if not num_slice:
                return 0
            if len(num_slice)==1:
                return num_slice[0]
            
            prev=num_slice[0]
            last=max(num_slice[0],num_slice[1])
        
            cur=max(prev,last)
            for i in range(2,len(num_slice)):
                cur=max(prev+num_slice[i],last)
                prev=last
                last=cur
            return cur
        return max(subproblem(nums[1:]),subproblem(nums[0:len(nums)-1]))
