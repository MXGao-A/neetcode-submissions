from collections import Counter,deque
import heapq as hp
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_dict=Counter(tasks)
        ans=0
        lis=[]
        for x,y in count_dict.items():
            lis.append((-y,x))
        hp.heapify(lis)
        heap=lis
        queue=deque([])
        time=0
        while heap or queue:
            while queue and queue[0][0]<=time:
                ready_time, count, task = queue.popleft()
                hp.heappush(heap,(count,task))
            if heap:
                count,task=hp.heappop(heap)
                count+=1
                if count<0:
                    queue.append((time+n+1,count,task))
            if not heap:
                if not queue:
                    time+=1
                    break
                    
                if time<queue[0][0]:
                    #idle
                    pass
            time+=1
        return time


            
