#15-20 minutes
class Solution:
    def isValid(self, s: str) -> bool:
        n = 0
        n = 0
        while n < len(s) - 1:
            if s[n] == "(" and s[n + 1] == ")":
                s = s[0:n] + s[n + 2:len(s)]
                n = 0
            elif s[n] == "[" and s[n + 1] == "]":
                s = s[0:n] + s[n + 2:len(s)]
                n = 0
            elif s[n] == "{" and s[n + 1] == "}":
                s = s[0:n] + s[n + 2:len(s)]
                n = 0
            else:
                n = n + 1
        return s == ''