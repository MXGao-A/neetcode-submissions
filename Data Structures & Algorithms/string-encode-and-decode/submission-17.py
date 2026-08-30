class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+"#"+s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        has_start=False
        i=0
        j=0
        while i < len(s):
            cur=""
            len_str=s[i]
            j=i+1
            if j>=len(s):
                break
            while s[j]!="#":
                len_str+=s[j]
                j+=1
    
            length=int(len_str)
            if length>=1:
                for k in range(1,length+1):
                    cur+=s[j+k]
            res.append(cur)
            i=j+length+1
        return res