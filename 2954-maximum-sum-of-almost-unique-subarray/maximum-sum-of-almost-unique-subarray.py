class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        res = 0
        for i in range(len(nums) - k + 1):
            if len(set(nums[i:i+k])) >= m:
                res = max(res, sum(nums[i:i+k]))
        return res
#see python solution
'''class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        seen = collections.defaultdict(int)
        s = 0
        res = 0
        for i in range(k):
            s += nums[i]
            seen[nums[i]] += 1
        if len(seen) >= m:
            res = s
        for i in range(k, len(nums)):
            s += nums[i]
            s -= nums[i - k]
            seen[nums[i]] += 1
            seen[nums[i - k]] -= 1
            if seen[nums[i - k]] == 0:
                del seen[nums[i - k]]
            if len(seen) >= m:
                res = max(res, s)
        return res'''


        