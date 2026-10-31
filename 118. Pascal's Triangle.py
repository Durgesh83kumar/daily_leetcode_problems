class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def generateRow(row):
            ans = 1
            ansRow = []
            ansRow.append(ans)
            for col in range(1,row):
                ans = ans * (row-col)
                ans = ans / col
                ansRow.append(ans)
            return ansRow
        ans = []
        for i in range(1,numRows+1):
            ans.append(generateRow(i))
        return ans