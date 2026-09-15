class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0
        h = 0
        while l<len(nums):
            if nums[l] != 0:
                nums[l],nums[h] = nums[h],nums[l]
                l += 1
                h += 1
            else:
                l += 1