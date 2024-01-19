class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_count = [0] * 100000
        for i in range(len(nums)):
            num_count[nums[i]] += 1
        
        for i in range(len(nums)):
            if num_count[nums[i]] == 1:
                return nums[i]
