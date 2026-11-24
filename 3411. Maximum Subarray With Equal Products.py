from math import gcd, lcm


class Solution:
    def maxLength(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        overall_lcm = 1
        max_val = 0
        for x in nums:
            overall_lcm = lcm(overall_lcm, x)
            if x > max_val:
                max_val = x

        max_prod_bound = overall_lcm * max_val

        for i in range(n):
            prod = 1
            curr_gcd = 0
            curr_lcm = 1

            for j in range(i, n):
                x = nums[j]
                prod *= x
                curr_gcd = gcd(curr_gcd, x)
                curr_lcm = lcm(curr_lcm, x)

                if prod == curr_gcd * curr_lcm:
                    ans = max(ans, j - i + 1)

                if prod > max_prod_bound:
                    break

        return ans