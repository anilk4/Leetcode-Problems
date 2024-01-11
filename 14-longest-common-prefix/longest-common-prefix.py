class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return output
                
            output += s[i]
        return output
