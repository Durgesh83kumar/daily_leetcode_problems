class Solution(object):
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = {grid[i][j]}
                    continue

                curr = set()
                val = grid[i][j]

                if i > 0:
                    for x in dp[j]:
                        curr.add(x ^ val)

                if j > 0:
                    for x in dp[j - 1]:
                        curr.add(x ^ val)

                dp[j] = curr

        return min(dp[-1])        