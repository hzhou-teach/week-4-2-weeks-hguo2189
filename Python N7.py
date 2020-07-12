#10-15 minutes
class Solution:
    def reverse(self, x: int) -> int:
        steps = 0
        while steps >= 0:
            digits = []
            save = x
            while save > 0:
                digits.append(save%10)
                save = save // 10
            y = 0
            for digit in digits:
                y = y * 10 + digit
            if x == y:
                return steps
            
            digits = []
            save = x
            while save > 0:
                digits.insert(0, save%10)
                save = save // 10
            y = 0
            for digit in digits:
                y = y * 10 + digit
            x = x + y
            steps += 1