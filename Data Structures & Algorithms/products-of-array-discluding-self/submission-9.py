
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        left_prod = [1] * n
        right_prod = [1] * n

        # Inclusive left prefix product
        left_prod[0] = nums[0]
        for i in range(1, n):
            left_prod[i] = left_prod[i-1] * nums[i]

        # Inclusive right suffix product
        right_prod[n-1] = nums[n-1]
        for j in range(n-2, -1, -1):
            right_prod[j] = right_prod[j+1] * nums[j]

        ans = [1] * n

        for i in range(n):
            if i > 0:
                ans[i] *= left_prod[i-1]
            if i < n-1:
                ans[i] *= right_prod[i+1]

        return ans
