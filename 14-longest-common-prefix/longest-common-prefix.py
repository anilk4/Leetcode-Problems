class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ''
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return out
            out += s[i]
        return out