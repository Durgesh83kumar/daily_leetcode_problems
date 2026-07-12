class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Sort unique elements
        sorted_unique = sorted(set(arr))

        # Assign ranks
        rank = {}
        for i, num in enumerate(sorted_unique):
            rank[num] = i + 1

        # Replace each element with its rank
        return [rank[num] for num in arr]