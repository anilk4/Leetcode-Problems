class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new = [0]*len(nums)*2
        n = len(nums)
        for i in range(len(nums)):
            new[i], new[i+n] = nums[i], nums[i]
        return new
        