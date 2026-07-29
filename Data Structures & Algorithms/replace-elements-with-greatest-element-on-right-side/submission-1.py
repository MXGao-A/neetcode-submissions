class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_right_max=arr[len(arr)-1]
        for i in range(len(arr)-1,-1,-1):
            if i == len(arr)-1:
                arr[i]=-1
            else:
                cur_val=arr[i]
                arr[i]=cur_right_max
                cur_right_max=max(cur_right_max,cur_val)
        return arr
