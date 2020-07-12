#10-15 minutes
#Bug fixes
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = int(a) + int(b)
        digits = []
        while n != 0:
            x = n % 10
            n = n // 10
            if x >= 2:
                n = n + 1
                x = x - 2
            digits.insert(0, x)
        for digit in digits:
            n = n * 10 + digit
        return str(n)