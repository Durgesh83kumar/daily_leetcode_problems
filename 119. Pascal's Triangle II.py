class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = rowIndex+1
        ans = 1
        ansRow = []
        ansRow.append(ans)
        for col in range(1,row):
            ans = ans * (row-col)
            ans = ans / col
            ansRow.append(ans)
        return ansRow