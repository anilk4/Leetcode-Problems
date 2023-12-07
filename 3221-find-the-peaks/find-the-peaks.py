class Solution:
    def findPeaks(self, a: List[int]) -> List[int]:
        res = []
        for i in range(1,len(a)-1):
            if a[i]>a[i-1] and a[i]>a[i+1]:
                res.append(i)
        return res