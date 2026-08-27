class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped={}
        for per_str in strs:
            str_freq={}
            for s in per_str:
                str_freq[s]=str_freq.get(s,0)+1
            
            key=tuple(sorted(str_freq.items()))
            if key not in grouped:
                grouped[key]=[per_str]
            else:
                grouped[key].append(per_str)
        return list(grouped.values())