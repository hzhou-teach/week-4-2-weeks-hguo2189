#10-15 minutes
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = 0
        ans = 0
        while n <= len(nums):
            if n == 0:
                if target <= nums[n]:
                    ans = n
                    n = len(nums) + 1
                else:
                    n = n + 1
            elif n == len(nums):
                ans = n
                n = len(nums) + 1
            else:
                if nums[n - 1] < target <= nums[n]:
                    ans = n
                    n = len(nums) + 1
                else:
                    n = n + 1
        return ans