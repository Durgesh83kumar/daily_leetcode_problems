class Solution(object):
    def canReach(self, start, target):
        """
        :type start: List[int]
        :type target: List[int]
        :rtype: bool
        """
        return (start[0] + start[1]) % 2 == (target[0] + target[1]) % 2