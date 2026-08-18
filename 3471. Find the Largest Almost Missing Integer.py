class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if k == 1:
            d = {}
            for x in nums:
                if x not in d:
                    d[x] = 1
                else:
                    d[x] += 1
            maximum = -1
            for key, val in d.items():
                if val == 1 and key > maximum:
                    maximum = key
            return maximum

        if k == n:
            return max(nums)
        
        if 1<k<n:
            if nums[0] not in nums[1:]:
                if nums[0]>nums[n-1]:
                    return nums[0]
                else:
                    if nums[n-1] not in nums[:n-1]:
                        return nums[n-1]
                    return nums[0]
            if nums[n-1] not in nums[:n-1]:
                return nums[n-1]
        
        return -1