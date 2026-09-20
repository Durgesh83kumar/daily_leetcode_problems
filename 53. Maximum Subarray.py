class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n^3)
        # max_sum = float('-inf')
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)): 
        #         current_sum = 0
        #         for k in range(i,j+1):
        #             current_sum += nums[k]
        #             if current_sum>max_sum:
        #                 max_sum = current_sum
        # return max_sum

        # O(n^2)
        # max_sum = float('-inf')
        # for i in range(len(nums)):
        #     current_sum = 0
        #     for j in range(i,len(nums)):
        #         current_sum += nums[j]
        #         if current_sum>max_sum:
        #             max_sum = current_sum
        # return max_sum

        # O(n) # Kadane's Algorithm
        current_sum = 0
        max_sum = float('-inf')
        for i in range(len(nums)):
            current_sum = current_sum + nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum<0:
                current_sum = 0

        return max_sum