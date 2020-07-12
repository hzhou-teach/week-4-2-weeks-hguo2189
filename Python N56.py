#30-35 minutes
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = 0
        while n < len(intervals) - 1:
            itvone = intervals[n]
            itvtwo = intervals[n + 1]
            if itvone[1] >= itvtwo[0]:
                if itvone[1] >= itvtwo[1]:
                    intervals.pop(n + 1)
                else:
                    intervals.pop(n + 1)
                    intervals.pop(n)
                    intervals.insert(n, [itvone[0],itvtwo[1]])
            else:
                n += 1
        return intervals