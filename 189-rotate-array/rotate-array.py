class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < k:
            k = k % len(nums)
        last_k_elements = nums[-k:]


        nums[k:] = nums[:-k]

        nums[:k] = last_k_elements