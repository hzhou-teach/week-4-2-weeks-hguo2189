#35-40 minutes
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        x = 0
        while x < len(nums) - 1:
            if nums[0] < 1:
                nums = nums[1:len(nums)]
            elif nums[0] > 1:
                return 1
            else:
                if nums[x] >= nums[x + 1] - 1:
                    x += 1
                else:
                    return nums[x] + 1
        if len(nums) == 0:
            return 1
        elif len(nums) == 1:
            if nums[0] == 1:
                return 2
            else:
                return 1
        else:
            return nums[len(nums) - 1] + 1