#20-25 minutes
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        numbers = []
        x = 2
        y = 1
        numof = 1
        digit = 0
        while x <= n and n != 1:
            while y != 0:
                digit = y % 10
                y = y // 10
                if digit == y % 10:
                    numof = numof + 1
                else:
                    numbers.insert(0, 10 * numof + digit)
                    numof = 1
            for number in numbers:
                y = y * 100 + number
            x = x + 1
            numof = 1
            digit = 0
            numbers = []
        return str(y)