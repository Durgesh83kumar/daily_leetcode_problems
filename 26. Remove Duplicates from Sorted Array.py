class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_arr = []
        index = 0

        for x in nums:
            if(x not in n_arr):
                n_arr.append(x)

                nums[index]=x
                index += 1
        return index