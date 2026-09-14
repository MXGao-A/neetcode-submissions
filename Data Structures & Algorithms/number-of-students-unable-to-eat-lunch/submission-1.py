from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt=0
        q=deque(students)
        no_matched=0
        while q and no_matched<=len(q):
            if q[0]==sandwiches[0]:
                q.popleft()
                sandwiches.pop(0)
                no_matched=0
            else:
                element=q[0]
                q.popleft()
                q.append(element)
                no_matched+=1
        return len(q)
            