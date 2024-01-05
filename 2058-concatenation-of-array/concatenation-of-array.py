class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [0]*n*2

        for i in range(n):
            out[i] = nums[i]
            out[i+n] = nums[i]

        return out
        