class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def vowel(s):
            small = {'a':0 , 'e':0, 'i':0, 'o':0, 'u':0,'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
            for i in s:
                if i in small:
                    small[i] += 1
            return sum(small.values())
        n = len(s) // 2
        first = s[:n]
        second = s[n:]
        return vowel(first) == vowel(second)
        