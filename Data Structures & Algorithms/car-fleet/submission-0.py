class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[(pos,speed) for pos,speed in zip(position,speed)]
        cars.sort(reverse=True,key=lambda x:x[0])
        lis=[]
        for pos,speed in cars:
            if not lis:
                lis.append((target-pos)/speed)
            else:
                if (target-pos)/speed<=lis[-1]:
                    pass
                else:
                    lis.append((target-pos)/speed)
        return len(lis)