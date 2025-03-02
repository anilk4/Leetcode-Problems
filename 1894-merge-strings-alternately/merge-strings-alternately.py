class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = ""
        l1, l2 = 0, 0

        while (l1 < len(word1) or l2 < len(word2)):
            if l1 < len(word1):
                merge += word1[l1]
            if l2 < len(word2):
                merge += word2[l2]
            l1 += 1
            l2 += 1
        return merge