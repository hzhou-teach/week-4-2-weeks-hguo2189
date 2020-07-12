#25 minutes
#Bug fixes also took a while
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        n = 0
        while n < len(nums):
            if nums[n] == target and first == -1:
                first = n
                n = n + 1
            elif nums[n] == target:
                last = n
                n = n + 1
            else:
                n = n + 1
        if first != -1 and last == -1:
            last = first
        return [first, last]