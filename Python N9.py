#5-10 minutes
class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = []
        save = x
        while x > 0:
            digits.append(x%10)
            x = x // 10
        y = 0
        for digit in digits:
            y = y * 10 + digit
        return save == y