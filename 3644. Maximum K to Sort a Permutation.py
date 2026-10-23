class Solution(object):
    def sortPermutation(self, nums):
        ans = -1

        for i, num in enumerate(nums):
            if i != num:
                ans &= num

        return max(ans, 0)