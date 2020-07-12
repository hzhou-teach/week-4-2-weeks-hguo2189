#25-30 minutes
class Solution:
    def myPow(self, x: float, n: int) -> float:
        num = 1
        if x == -1 or x == 1:
            if n % 2 == 1:
                return x
            else:
                return 1
        elif n < 0:
            while n < 0:
                num = num / x
                n = n + 1
                if num == 0:
                    n = 0
        elif n > 0:
            while n > 0:
                num = num * x
                n = n - 1
                if num == 0:
                    n = 0
        return num