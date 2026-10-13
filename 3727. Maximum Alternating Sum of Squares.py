class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            nums[i] = nums[i]**2

        nums.sort(reverse=True)

        if len(nums) % 2 == 0:
            ans = 0
            j = 0
            k = 0
            while j<len(nums)//2:
                ans += nums[k]
                k += 1
                j += 1
            while j < len(nums):
                ans -= nums[k]
                k += 1
                j += 1

        else:
            ans = 0
            j = 0
            k = 0
            while j<=len(nums)//2:
                ans += nums[k]
                k += 1
                j += 1
            while j < len(nums):
                ans -= nums[k]
                k += 1
                j += 1

        return ans