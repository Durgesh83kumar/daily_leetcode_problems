class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        n = len(stones)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        dp = prefix[n]

        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i + 1] - dp)

        return dp