class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # prefix[j]-prefix[i-1]//k==0
        # 对于每一个j,找到i-1使得他们除以k的余数相同，再累加每一个j的值
        ans=0
        hash_map={0:1}
        prefix=0
        for num in nums:
            prefix+=num
            ans+=hash_map.get(prefix%k,0)
            hash_map[prefix%k]=hash_map.get(prefix%k,0)+1
        return ans
