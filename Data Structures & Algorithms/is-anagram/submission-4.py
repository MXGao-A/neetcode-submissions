class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic={}
        for per_s in s:
            if per_s not in s_dic:
                s_dic[per_s]=1
            else:
                s_dic[per_s]+=1
        t_dic={}
        for per_t in t:
            if per_t not in t_dic:
                t_dic[per_t]=1
            else:
                t_dic[per_t]+=1
        if len(list(t_dic.keys()))!=len(list(s_dic.keys())):
            return False
        for key in s_dic:
            if not key in t_dic or t_dic[key]!=s_dic[key]:
                return False
        return True