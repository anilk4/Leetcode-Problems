class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0]*(n+1)
        missing, duplicate = 0, 0

        for num in nums:
            arr[num] += 1
        
        for i in range(1, len(arr)):
            if arr[i] == 2:
                duplicate = i
            if arr[i] == 0:
                missing = i
        return [duplicate, missing]
