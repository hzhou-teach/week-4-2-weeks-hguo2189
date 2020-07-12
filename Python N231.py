#5 minutes
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            if n / 2 != n // 2:
                n = 0
            else:
                n = n / 2
        return n == 1