class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        dictt = {}
        for s in strs:
            key = ''.join(sorted(s)) #aet
            if key in dictt:
                dictt[key] = dictt[key] + [s]
            else:
                dictt[key] = [s] 

        for value in dictt.values():
            final.append(value)
        return final
        