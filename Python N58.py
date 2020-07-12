#20-25 minutes
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = 0
        last = "filler"
        wordl = 0
        while n < len(s):
            if s[n:n + 1] == ' ':
                n = n + 1
                last = "space"
            else:
                if last == "space":
                    wordl = 1
                    n = n + 1
                    last = "character"
                else:
                    wordl = wordl + 1
                    n = n + 1
                    last = "character"
        return wordl