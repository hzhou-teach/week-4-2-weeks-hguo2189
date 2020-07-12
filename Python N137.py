#20-25 minutes
#Very similar to first one 
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        nums.sort()
        while n < 3:
            if len(nums) == 1:
                return nums[0]
            elif n == 0:
                x = nums[n]
                n = n + 1
            elif n == 1:
                if x == nums[n]:
                    nums = nums[3:len(nums)]
                    n = 0
                else:
                    return x