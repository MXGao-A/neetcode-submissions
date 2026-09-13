class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_to_check={}
        for s in s1:
            freq_to_check[s]=freq_to_check.get(s,0)+1
        
        cur_freq={}
        left=0
        s1_len=len(s1)
        for right,s in enumerate(s2):
            if right>=s1_len:
                cur_freq[s2[left]]-=1
                left+=1
            cur_freq[s]=cur_freq.get(s,0)+1
            
            if right-left+1==s1_len:
                match_cnt=0
                print(freq_to_check,cur_freq)
                for key in freq_to_check.keys():
                    if key not in cur_freq or freq_to_check[key]!=cur_freq[key]:
                        break
                    else:
                        match_cnt+=1
                if match_cnt==len(list(freq_to_check.keys())):
                    return True

        return False