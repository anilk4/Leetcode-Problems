class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        l = len(s)
        count1 = 0
        for i in s:
            if i == "1":
                count1 += 1
        
        count0 = l - count1
       
        res = '1'*(count1-1) + '0'*(count0) + '1'
        return res