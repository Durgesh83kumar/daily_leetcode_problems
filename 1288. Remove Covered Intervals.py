class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:(x[0],-x[1]))
        ans = 1
        max_end = intervals[0][1]
        for start, end in intervals[1:]:
            if end<=max_end:
                continue
            ans += 1
            max_end = end
        return ans