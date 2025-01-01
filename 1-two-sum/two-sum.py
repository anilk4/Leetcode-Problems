class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        
        for i, val in enumerate(nums):
            current = target - val
            if current in store:
                return [i, store[current]]
            else:
                store[val] = i
        return -1
