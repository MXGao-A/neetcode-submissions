class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums)==1:
            return 1 if nums[0]==k else 0

       
        count=0
        prefix=0
        hash_map={0:1} 
        #sum=prefix[i]-prefix[j-1]=k
        #so at i, we can see how many j-1 satisfy
        for i,num in enumerate(nums):
            prefix+=num

            if (prefix-k) in hash_map:
                count+=hash_map[prefix-k]

            hash_map[prefix]=hash_map.get(prefix,0)+1
        return count