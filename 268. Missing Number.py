class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        if nums[0] != 0:
            return 0
        for i in range(n-1):
            if nums[i+1] - nums[i] > 1:
                return i+1
        if nums[-1] < n:
            return nums[-1]+1