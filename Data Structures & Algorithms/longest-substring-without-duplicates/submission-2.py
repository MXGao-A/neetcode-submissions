class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        len_longest_substring=-float("inf")
        cur_str=""
        for right, c in enumerate(s):
            if c in cur_str:
                while c in cur_str:
                    cur_str=cur_str[1:]
                cur_str+=c
                len_longest_substring=max(len_longest_substring,len(cur_str))
            else:
                cur_str+=c
                len_longest_substring=max(len_longest_substring,len(cur_str))
        return len_longest_substring if len_longest_substring!=-float("inf") else 0

