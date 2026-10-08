import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        heap=[]
        for point in points:
            distance=point[0]**2+point[1]**2
            heap.append((-distance,point))
        heapq.heapify(heap)
        while len(heap)>k:
            heapq.heappop(heap)
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res

