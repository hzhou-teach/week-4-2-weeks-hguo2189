#30-35 minutes
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = 0
        while n < len(s):
            sub = s[n]
            if sub.isalnum():
                n = n + 1
            else:
                s = s[0:n] + s[n + 1:len(s)]
        n = 0
        while n < len(s) - n:
            sub = s[len(s) - n - 1]
            subtwo = s[n]
            if sub.lower() == subtwo.lower():
                n = n + 1
            else:
                n = len(s) + 1
        if n == len(s) + 1:
            return 1 == 0
        else:
            return 1 == 1