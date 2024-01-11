class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        maxi = 0
        left = 0
        right = 1
        while right < len(nums):
            if nums[right] > nums[left]:
                current = nums[right] - nums[left]
                if current > maxi:
                    maxi = current
                right += 1
            else:
                left = right
                right += 1

        return maxi
