class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # smallest = min(nums)
        # largest = max(nums)
        smallest = nums[0]
        largest = nums[0]
        for i in range(1,len(nums)):
            if nums[i]<smallest:
                smallest = nums[i]
            elif nums[i]>largest:
                largest = nums[i]
        while smallest != 0:
            temp = smallest
            smallest = largest % smallest
            largest = temp
        return largest