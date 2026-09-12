class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        longest=0
        chars=set()
        for right, c in enumerate(s):
            while c in chars:
                chars.remove(s[left])
                left+=1
                
            chars.add(c)
            longest=max(longest,right-left+1)
        return longest

