class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lst = []
        for i in range(len(nums)):
            a = max(nums[:i+1])
            b = min(nums[i:])
            if a-b<=k:
                lst.append(i)
        
        if lst:
            return min(lst)
        else:
            return -1