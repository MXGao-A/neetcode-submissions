class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=[]
        cur_add=1
        for i in range(len(digits)-1,-1,-1):
            if digits[i]+cur_add<10:
                cur_sum=digits[i]+cur_add
                cur_add=0
                res.append(cur_sum)
            elif digits[i]+cur_add==10:
                cur_sum=(digits[i]+cur_add)%10
                cur_add=1
                res.append(cur_sum)
        if cur_add:
            res.append(1)
        return res[::-1]