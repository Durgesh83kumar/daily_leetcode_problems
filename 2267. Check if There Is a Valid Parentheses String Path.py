class Solution(object):

    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """

        m = len(grid)
        n = len(grid[0])

        dp = [[set() for _ in range(n)] for _ in range(m)]

        if grid[0][0] == '(':
            dp[0][0].add(1)
        else:
            return False

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                prev = set()

                if i > 0:
                    prev |= dp[i - 1][j]

                if j > 0:
                    prev |= dp[i][j - 1]

                change = 1 if grid[i][j] == '(' else -1

                for balance in prev:
                    new_balance = balance + change

                    if new_balance >= 0:
                        dp[i][j].add(new_balance)

        return 0 in dp[m - 1][n - 1]
        