class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        maxi = 0
        l = 0
        r = 1
        while r < len(nums):
            if nums[r] > nums[l]:
                current = nums[r] - nums[l]
                maxi = max(maxi, current)
                r += 1
            else:
                l = r
                r += 1
                
        return maxi
