class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        acc=0
        left=0
        cnt=0
        for right, num in enumerate(arr):
            if right>=k:
                acc-=arr[left]
                left+=1
            
            acc+=arr[right]
            if (right-left+1)==k and (acc/k)>=threshold:
                print(acc,num)
                cnt+=1
            else:
                pass
        return cnt
