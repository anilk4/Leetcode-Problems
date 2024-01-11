class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        for i, num in enumerate(nums):
            val = target - num
            if val in dictt:
                return [dictt[val], i]
            else:
                dictt[num] = i