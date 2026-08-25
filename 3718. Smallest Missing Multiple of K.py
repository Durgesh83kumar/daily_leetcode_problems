class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pi = []
        s = k
        for x in nums:
            if x%s==0:
                pi.append(x)
        if s not in pi:
            return s
        else:
            for i in range(len(pi)):
                if (2+i)*s not in pi:
                    return (2+i)*s
        return max(pi) + k