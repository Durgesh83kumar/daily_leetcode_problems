class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_elt = max(nums)
        ans = 0
        for i in range(len(nums)):
            ans = ans + (max_elt - nums[i])
        return ans