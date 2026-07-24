class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAXX = 2048

        dp = [False] * MAXX
        dp[0] = True

        for _ in range(3):
            nxt = [False] * MAXX
            for x in range(MAXX):
                if dp[x]:
                    for num in nums:
                        nxt[x ^ num] = True
            dp = nxt

        return sum(dp)