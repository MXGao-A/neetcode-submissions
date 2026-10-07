class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def dfs(cur_list, cur_sum, index):
            if cur_sum == target:
                res.append(cur_list[:])
                return

            if cur_sum > target:
                return

            for i in range(index, len(nums)):
                num = nums[i]

                cur_list.append(num)
                cur_sum += num

                dfs(cur_list, cur_sum, i)

                cur_list.pop()
                cur_sum -= num

        dfs([], 0, 0)
        return res

        