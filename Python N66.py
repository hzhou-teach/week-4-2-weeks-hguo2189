#30 minutes
#Had to rewrite code since I didn't really know what it was asking for before
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = 0
        for digit in digits:
            x = x * 10 + digit
        x = x + 1
        digits = []
        while x != 0:
            digits.insert(0, x % 10)
            x = x // 10
        return digits