class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            total = 0
            n = nums[i]
            while n != 0:
                d = n%10
                n = n//10
                total += d
            if total == i:
                return i
        return -1 