class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)  # Modify nums1 in place
        nums1.sort()  # Sort the merged list
        
        n = len(nums1)
        
        if n % 2 == 0:
            # If the length is even, take the average of the two middle elements
            mid1 = n // 2
            mid2 = mid1 - 1
            median = (nums1[mid1] + nums1[mid2]) / 2
        else:
            # If the length is odd, the median is the middle element
            median = nums1[n // 2]

        return median