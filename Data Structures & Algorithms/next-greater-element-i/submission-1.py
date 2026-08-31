class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        stack=[]
        next_greater_map={}
        for i,num in enumerate(nums2):
            if not stack:
                stack.append((i,num))
            elif num<stack[-1][1]:
                stack.append((i,num))
            else:
                while stack and num>stack[-1][1]:
                    element=stack.pop()
                    next_greater_map[element[1]]=num
                stack.append((i,num))
        for num in nums1:
            res.append(next_greater_map.get(num,-1))
        return res