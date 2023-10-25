class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p = len(s)
        length = 0

        while p > 0:
            p -= 1

            if s[p] != ' ':
                length += 1
            elif length > 0:
                return length
        return length