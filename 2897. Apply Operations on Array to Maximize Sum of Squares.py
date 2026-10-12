
class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        cnt = [0] * 31

        for num in nums:
            for bit in range(31):
                if num & (1 << bit):
                    cnt[bit] += 1

        ans = 0

        for _ in range(k):
            num = 0

            for bit in range(31):
                if cnt[bit] > 0:
                    num |= 1 << bit
                    cnt[bit] -= 1

            ans = (ans + num * num) % MOD

        return ans