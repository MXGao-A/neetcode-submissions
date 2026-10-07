class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(index, cur):
            if index == len(nums):
                res.append(cur.copy())
                return

            # 选 nums[index]
            cur.append(nums[index])
            dfs(index+1,cur)

            cur.pop()
            dfs(index+1,cur)

            # 不选 nums[index]

        dfs(0, [])
        return res