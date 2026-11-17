class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix=0
        hash_map={0:-1}

        for j,num in enumerate(nums):
            prefix+=num

            remainder=prefix%k
            if (remainder) in hash_map and j-hash_map[remainder]>=2:
                return True
            if remainder not in hash_map:
                hash_map[remainder]=j
        return False