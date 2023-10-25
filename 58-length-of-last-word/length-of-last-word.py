class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1  # Start from the end of the string.

        # Skip any trailing spaces.
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        last = 0

        # Count the characters of the last word.
        while i >= 0 and s[i] != ' ':
            last += 1
            i -= 1

        return last

        