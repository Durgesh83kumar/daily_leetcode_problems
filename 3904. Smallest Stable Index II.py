class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        preffix_max = nums[0]
        suffix_min = [0]*n
        suffix_min[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i+1])
        
        for i in range(n):
            preffix_max = max(preffix_max,nums[i])

            if preffix_max-suffix_min[i] <= k:
                return i
        return -1