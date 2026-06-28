class Solution(object):
    def maxSum(self, nums, k, mul):
        """
        :type nums: List[int]
        :type k: int
        :type mul: int
        :rtype: int
        """
        nums.sort(reverse=True)
        i = 0
        total = 0
        while(i<k):
            if(mul>0):
                total = total + (nums[i]*mul)
                mul = mul - 1
                i = i + 1
            else:
                total = total + nums[i]
                mul = mul - 1
                i = i + 1

        return total