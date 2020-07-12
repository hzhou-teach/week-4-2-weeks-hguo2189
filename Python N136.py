#15-20 minutes
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        nums.sort()
        while n < 2:
            if n == 0:
                x = nums[n]
                n = n + 1
            elif n == 1:
                if len(nums) == 1:
                    return nums[0]
                elif x == nums[n]:
                    nums = nums[2:len(nums)]
                    n = 0
                else:
                    return x