#30-40 minutes
class Solution:
    def superPow(self, x: int, b: List[int]) -> int:
        remainders = [x % 1337]
        x = x % 1337
        remainder = x * x
        remainder = remainder % 1337
        while remainder != x:
            remainders.append(remainder)
            remainder = remainder * x
            remainder = remainder % 1337
        n = 0 
        for num in b:
            n = n * 10 + num
        n = n % len(remainders)
        return remainders[n - 1]