from bisect import bisect_left

class Solution(object):
    def gcdValues(self, nums, queries):
        maxVal = max(nums)

        # Frequency of every value
        freq = [0] * (maxVal + 1)
        for x in nums:
            freq[x] += 1

        # Count numbers divisible by d
        divisible = [0] * (maxVal + 1)
        for d in range(1, maxVal + 1):
            for multiple in range(d, maxVal + 1, d):
                divisible[d] += freq[multiple]

        # exact[d] = number of pairs whose gcd is exactly d
        exact = [0] * (maxVal + 1)

        for d in range(maxVal, 0, -1):
            pairs = divisible[d] * (divisible[d] - 1) // 2

            multiple = 2 * d
            while multiple <= maxVal:
                pairs -= exact[multiple]
                multiple += d

            exact[d] = pairs

        # Prefix count of sorted gcd values
        prefix = [0] * (maxVal + 1)
        total = 0
        for d in range(1, maxVal + 1):
            total += exact[d]
            prefix[d] = total

        # Answer queries
        ans = []
        for q in queries:
            ans.append(bisect_left(prefix, q + 1))

        return ans