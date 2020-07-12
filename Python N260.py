#25-30 minutes
#Similar to the first two
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = 0
        nums.sort()
        single = []
        while len(single) < 2:
            if len(nums) == 1:
                single.append(nums[0])
            elif n == 0:
                x = nums[n]
                n = n + 1
            elif n == 1:
                if x == nums[n]:
                    nums = nums[2:len(nums)]
                    n = 0
                else:
                    single.append(x)
                    nums = nums[1:len(nums)]
                    n = 0
        return single