class Solution(object):
    def minBishopMoves(self, source, target):
        """
        :type source: List[int]
        :type target: List[int]
        :rtype: int
        """
        if (source[0]+source[1])%2 != (target[0]+target[1])%2:
            return -1
        elif abs(source[0]-target[0]) == abs(source[1]-target[1]):
            return 1
        return 2