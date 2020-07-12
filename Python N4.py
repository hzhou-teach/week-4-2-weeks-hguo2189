#Didn't take too long in python, just took a while to figure out how to code it
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + nums2
        nums1.sort()
        n = len(nums1) - 1
        if n // 2 == n / 2:
            return nums1[int(n / 2)]
        else:
            return (nums1[int(n / 2 - 0.5)] + nums1[int(n / 2 + 0.5)]) / 2 