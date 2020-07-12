#20-25 minutes
#Took a while to fix the bugs
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = 0
        x = len(needle)
        save = len(haystack) - x
        while n <= len(haystack) - x:
            if needle == haystack[n:n + x]:
                save = n
                n = len(haystack) + 1
            else:
                n = n + 1
                save = save - 1
        return max(save, -1)     