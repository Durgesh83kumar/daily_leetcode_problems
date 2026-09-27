class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        while nums:
            cur = sorted(set(nums))
            ans.extend(cur)

            for x in cur:
                nums.remove(x)

        return ans
        