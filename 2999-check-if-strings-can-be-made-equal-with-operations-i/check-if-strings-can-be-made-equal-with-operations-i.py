class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return (s1[0]+s1[2] == s2[0]+s2[2] or s1[0]+s1[2] == s2[2]+s2[0]) and (s1[1]+s1[3] == s2[1]+s2[3] or s1[1]+s1[3] == s2[3]+s2[1])


'''class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1e={s1[0],s1[2]}
        s2e={s2[0],s2[2]}
        s1o={s1[1],s1[3]}
        s2o={s2[1],s2[3]}
        return s1e==s2e and s2o==s1o'''
         
        
        