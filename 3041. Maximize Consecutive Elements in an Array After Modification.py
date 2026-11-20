class Solution(object):
    def maxSelectedElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}
        ans = 0

        for num in sorted(nums):
            dp[num + 1] = dp.get(num, 0) + 1
            dp[num] = dp.get(num - 1, 0) + 1
            ans = max(ans, dp[num + 1], dp[num])

        return ans