class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        res = ''
        for i in s:
            if i not in res:
                res += i
            else:
                res = res[res.index(i)+1:] + i #Then consider new ele
            if len(res) > count:
                count = len(res)
        return count
#no need of DFS, Backtrack..just if ele not in then add it..else take from next 
            