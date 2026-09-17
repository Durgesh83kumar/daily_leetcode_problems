class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # TC: O(n)
        # # SC: O(n)
        # d = {}
        # for i in range(len(nums)):
        #     if nums[i] not in d:
        #         d[nums[i]] = 1
        #     else:
        #         d[nums[i]] += 1
        # for k, v in d.items():
        #     if v == 1:
        #         return k


        # optimize solution
        # TC: O(n)
        # SC: O(1)
        ans = 0
        for x in nums:
            ans ^= x

        return ans