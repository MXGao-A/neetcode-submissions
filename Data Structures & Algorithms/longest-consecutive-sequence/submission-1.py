class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set=set(nums)
        max_val=0
        for num in hash_set:
            cur_val=1
            if num-1 in hash_set:
                continue
            else:
                while num+1 in hash_set:    
                    cur_val+=1
                    num+=1
            max_val=max(cur_val,max_val)
        return max_val
