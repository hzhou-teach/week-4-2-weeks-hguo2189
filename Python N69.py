#5 minutes
class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0
        y = 0
        while y == 0:
            if n ** 2 > x:
                n = n - 1
                y = 1
            else:
                n = n + 1
        return n