class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        
        even1 = [s1[i] for i in range(0, len(s1), 2)]
        even2 = [s2[i] for i in range(0, len(s2), 2)]
        odd1 = [s1[i] for i in range(1, len(s1), 2)]
        odd2 = [s2[i] for i in range(1, len(s2), 2)]
        
        
        return sorted(odd1) == sorted(odd2) and sorted(even1) == sorted(even2)

#return sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2])
        