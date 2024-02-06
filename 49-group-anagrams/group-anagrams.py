class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        dictt = {}

        for s in strs:
            ele = "".join(sorted(s))
            if ele in dictt:
                dictt[ele] += [s]
            else:
                dictt[ele] = [s]
        for i in dictt.values():
            final.append(i)
        return final