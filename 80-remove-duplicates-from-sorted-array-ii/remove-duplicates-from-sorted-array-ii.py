class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        index = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[index-2]:
                nums[index] = nums[i]
                index += 1
        print(nums)
        return index