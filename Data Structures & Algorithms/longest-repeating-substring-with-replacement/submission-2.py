class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def find_max_key(func_map):
            cur_max=0
            max_key=""
            for key in func_map.keys():
                if func_map[key]>cur_max:
                    max_key=key
                    cur_max=max(cur_max,func_map[key])
            return max_key,cur_max
        left=0
        longest=0
        cur_map={}
        cur_len=0
        for right, c in enumerate(s):
            cur_map[c]=cur_map.get(c,0)+1
            cur_len+=1
            while (cur_len-find_max_key(cur_map)[1])>k:
                cur_len-=1
                cur_map[s[left]]-=1
                left+=1
               
            
            longest=max(longest,right-left+1)
            
            

        return longest
