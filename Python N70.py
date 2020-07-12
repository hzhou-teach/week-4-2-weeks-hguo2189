#20-25 minutes
class Solution:
    def climbStairs(self, n: int) -> int:
        n = max(min(n,45),1)
        ones = n
        twos = 0
        n = 0
        while ones >= 0:
            n = n + factorial(ones + twos) / factorial(ones) / factorial(twos)
            ones = ones - 2
            twos = twos + 1
        return int(n)