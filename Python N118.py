#30-40 minutes
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lione = [[1]]
        litwo = []
        item = 0
        row = 2
        while numRows >= row:
            save = row
            while row > 0:
                litwo.append(0)
                row = row - 1
            row = save
            lithree = lione[len(lione) - 1]
            while item < len(lithree):
                x = litwo[item] + lithree[item]
                litwo.pop(item)
                litwo.insert(item, x)
                x = litwo[item + 1] + lithree[item]
                litwo.pop(item + 1)
                litwo.insert(item + 1, x)
                item = item + 1
            lione.append(litwo)
            litwo = []
            item = 0
            row = row + 1
        if numRows == 0:
            return []
        else:
            return lione