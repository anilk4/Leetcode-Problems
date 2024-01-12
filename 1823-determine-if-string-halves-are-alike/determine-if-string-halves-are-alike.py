class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']

        while right > left:
            if s[left] in vowels:
                count += 1
            if s[right] in vowels:
                count -= 1
            left += 1
            right -= 1
        return count == 0