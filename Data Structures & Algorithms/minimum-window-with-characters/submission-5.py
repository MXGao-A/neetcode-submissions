class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_to_check={}
        cur_map={}
        for c in t:
            freq_to_check[c]=freq_to_check.get(c,0)+1
        left=0
        have=0
        min_length=float("inf")
        need=len(freq_to_check.keys())
        for right, c in enumerate(s):
            cur_map[c]=cur_map.get(c,0)+1
            if c in freq_to_check and freq_to_check[c]==cur_map[c]:
                have+=1
            while have==need:
                if right-left+1<min_length:
                    min_length=right-left+1
                    ans=s[left:left+min_length]
 
                cur_map[s[left]]-=1
                if s[left] in freq_to_check and cur_map[s[left]]<freq_to_check[s[left]]:
                    have-=1
                left+=1
        return ans if min_length!=float("inf") else ""