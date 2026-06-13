from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        nums = list(map(str, nums))

        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            return 0

        nums.sort(key=cmp_to_key(compare))

        ans = "".join(nums)

        return "0" if ans[0] == "0" else ans