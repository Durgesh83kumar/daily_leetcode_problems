class Solution(object):
    def longestArithmetic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # d[i] = nums[i] - nums[i-1]
        d = [0] * n
        for i in range(1, n):
            d[i] = nums[i] - nums[i - 1]

        # f[i] = longest arithmetic subarray ending at i
        f = [2] * n
        f[0] = 1
        for i in range(2, n):
            if d[i] == d[i - 1]:
                f[i] = f[i - 1] + 1

        # g[i] = longest arithmetic subarray starting at i
        g = [2] * n
        g[n - 1] = 1
        for i in range(n - 3, -1, -1):
            if d[i + 1] == d[i + 2]:
                g[i] = g[i + 1] + 1

        ans = 3

        for i in range(n):

            # No replacement
            ans = max(ans, f[i], g[i])

            # Extend left segment
            if i > 0:
                ans = max(ans, f[i - 1] + 1)

            # Extend right segment
            if i + 1 < n:
                ans = max(ans, g[i + 1] + 1)

            # Replace nums[i] to connect left and right
            if 0 < i < n - 1:
                diff = nums[i + 1] - nums[i - 1]

                if diff % 2 == 0:
                    diff //= 2
                    cur = 3

                    if i > 1 and d[i - 1] == diff:
                        cur += f[i - 1] - 1

                    if i < n - 2 and d[i + 2] == diff:
                        cur += g[i + 1] - 1

                    ans = max(ans, cur)

        return ans