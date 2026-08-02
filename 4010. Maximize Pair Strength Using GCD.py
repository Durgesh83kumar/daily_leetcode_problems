class Solution(object):
    def gc(self, a, b):
        while b != 0:
            temp = b
            b = a%b
            a = temp
        return a
    def maxPairStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bes = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                g = self.gc(nums[i], nums[j])
                stren = (nums[i]//g)*(nums[j]//g)
                if stren > bes:
                    bes = stren
        return bes
        