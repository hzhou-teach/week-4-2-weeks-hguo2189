#35-45 minutes
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = []
        n = 1
        x = 0
        sign = "+"
        while x < len(s):
            rows.append(n)
            x = x + 1
            if sign == "+":
                n = n + 1
                n = min(numRows, n)
            elif sign == "-":
                n = n - 1
                n = max(n, 1)
            if n == numRows:
                sign = "-"
            elif n == 1:
                sign = "+"
        x = 0
        n = 1
        st = ""
        while n <= numRows:
            while x < len(s):
                if rows[x] == n:
                    st = st + s[x]
                    x = x + 1
                else:
                    x = x + 1
            n = n + 1
            x = 0
        return st