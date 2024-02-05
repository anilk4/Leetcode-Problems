class Solution:
    def firstUniqChar(self, s: str) -> int:
        uni = {}
        for i in s:
            if i not in uni:
                uni[i] = 1
            else:
                uni[i] += 1
        for i, val in uni.items():
            if val == 1:
                return s.index(i)
        return -1
        