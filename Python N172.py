#5 minutes
class Solution:
    def trailingZeroes(self, n: int) -> int:
        exp = 1
        zeroes = 0
        while 5 ** exp <= n:
            zeroes = zeroes + n // (5 ** exp) 
            exp += 1
        return zeroes