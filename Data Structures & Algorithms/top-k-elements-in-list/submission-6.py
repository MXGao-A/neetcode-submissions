class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq={}
        # for num in nums:
        #     freq[num]=freq.get(num,0)+1

        # return [x[0] for x in sorted(freq.items(),key=lambda x:x[1],reverse=True)[:k]]

        #the solution above has a time complexity exceed the requirement.

        # freq={}
        # for num in nums:
        #     freq[num]=freq.get(num,0)+1
        # bucket=[[] for _ in range(len(nums)+1)]
        # for num, count in freq.items():
        #     bucket[count].append(num)
        # ans=[]
        # for count in range(len(nums),0,-1):
        #     for num in bucket[count]:
        #         ans.append(num)
            
        #     if len(ans)==k:
        #         return ans

        freq={}
        heap=[]
        res=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for key,value in freq.items():
            heap.append((value,key))
        heapq.heapify(heap)
        while len(heap)>k:
            heapq.heappop(heap)
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res
