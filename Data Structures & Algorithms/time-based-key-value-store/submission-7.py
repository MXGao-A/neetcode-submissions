class TimeMap:

    def __init__(self):
        self.time_map={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key]=[(timestamp,value)]
        else:
            self.time_map[key].append((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
            
        array_search=self.time_map[key]
    
        left,right=0,len(array_search)-1
        cand=""
        while left<=right:
            
            mid=(left+right)//2
            if array_search[mid][0]==timestamp:
                return array_search[mid][1]
            elif array_search[mid][0]>timestamp:
                right=mid-1
            elif array_search[mid][0]<timestamp:
                cand=array_search[mid][1]
                left=mid+1
        return cand
