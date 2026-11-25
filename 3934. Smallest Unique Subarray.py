class Solution(object):
    def smallestUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        base = 100003
        mod = 10**9 + 7

        powers = [1] * (n + 1)
        for i in range(1, n + 1):
            powers[i] = (powers[i - 1] * base) % mod

        def has_unique_of_length(length):
            if length > n:
                return False

            h = 0
            for i in range(length):
                h = (h * base + nums[i]) % mod

            counts = {h: 1}
            high_pow = powers[length - 1]

            for i in range(1, n - length + 1):
                out_val = (nums[i - 1] * high_pow) % mod
                h = (h - out_val + mod) % mod
                h = (h * base + nums[i + length - 1]) % mod
                counts[h] = counts.get(h, 0) + 1

            return any(freq == 1 for freq in counts.values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique_of_length(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans