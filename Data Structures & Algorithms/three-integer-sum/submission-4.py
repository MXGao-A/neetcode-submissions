class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums=sorted(nums)
        res=[]
        for i, num in enumerate(sorted_nums):
            if i>=1 and sorted_nums[i]==sorted_nums[i-1]:
                continue
            else:
                left,right=i+1,len(sorted_nums)-1
                target=0-sorted_nums[i]
                while left<right:
                    while right>left>=i+2 and sorted_nums[left]==sorted_nums[left-1]:
                        left+=1
                    while left<right<=len(sorted_nums)-2 and sorted_nums[right]==sorted_nums[right+1]:
                        right-=1
                    if left>=right:
                        break
                    if sorted_nums[left]+sorted_nums[right]>target:
                        right-=1
                    elif sorted_nums[left]+sorted_nums[right]<target:
                        left+=1
                    else:
                        res.append([sorted_nums[i],sorted_nums[left],sorted_nums[right]])
                        left+=1
                        right-=1
                        
        return res
