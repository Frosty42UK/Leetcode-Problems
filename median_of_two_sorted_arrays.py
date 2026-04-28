class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged = sorted(merged)
        length = len(merged)
        if length % 2 != 0:  # odd length
            return merged[int(length / 2)]
        else:
            return (merged[int(length / 2 - 1)] + merged[int(length / 2)]) / 2

        return 0.00