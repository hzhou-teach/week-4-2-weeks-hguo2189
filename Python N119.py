#15-20 minutes
#Very similar to first one
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lione = [[1]]
        litwo = []
        item = 0
        row = 2
        while rowIndex + 1 >= row:
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
        if rowIndex == 0:
            return [1]
        else:
            return lione[min(33,rowIndex)]