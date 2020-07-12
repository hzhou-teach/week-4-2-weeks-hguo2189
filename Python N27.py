#5 minutes
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        while n < len(nums):
            if nums[n] == val:
                nums.pop(n)
            else:
                n = n + 1
        return len(nums)