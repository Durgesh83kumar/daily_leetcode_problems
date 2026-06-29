class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        res = []
        n = len(intervals)
        dummy = intervals[0]

        for i in range(1, n):
            if(dummy[1]<intervals[i][0]):
                res.append(dummy)
                dummy = intervals[i]
            else:
                dummy[0] = min(intervals[i][0], dummy[0])
                dummy[1] = max(intervals[i][1], dummy[1])

        res.append(dummy)
        return res