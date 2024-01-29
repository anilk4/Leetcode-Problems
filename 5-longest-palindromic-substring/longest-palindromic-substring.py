class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1

            while right > left:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True
        
        for last in range(len(s), 0, -1):
            for first in range(len(s) - last + 1):
                if check(first, first + last):
                    return s[first : first + last]
        return ""