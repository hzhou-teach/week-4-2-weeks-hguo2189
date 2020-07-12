#30-35 minutes
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        x = 0
        while x == 0:
            if n <= 0:
                nums.sort()
                x = 1
            elif nums[n] <= nums[n - 1]:
                n += -1
            elif nums[n] > nums[n - 1]:
                checker = nums[n - 1]
                subnums = nums[n - 1:len(nums)]
                subnums.sort()
                del nums[n - 1:len(nums)]
                n = 0
                while n != -1:
                    if subnums[n] <= checker:
                        n += 1
                    elif subnums[n] > checker:
                        checker = subnums[n]
                        subnums.pop(n)
                        subnums.insert(0, checker)
                        n = -1
                for num in subnums:
                    nums.append(num)
                x = 1
        return nums
            