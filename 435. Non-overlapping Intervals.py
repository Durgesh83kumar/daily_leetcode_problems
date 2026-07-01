class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[1]) # sort by end time
        n = len(intervals)
        prev_end_term = intervals[0][1]
        count = 1
        for i in range(1, n):
            if(intervals[i][0] >= prev_end_term):
                count = count + 1
                prev_end_term = intervals[i][1]
        return n-count


# 2nd methond
        # intervals.sort(key=lambda x:x[0]) # sort by start time
        # n = len(intervals)
        # prev_end_term = intervals[0][1]
        # count = 0
        # for start, end in intervals[1:]:
        #     if(start >= prev_end_term):
        #         prev_end_term = end
        #     else:
        #         count = count + 1
        #         prev_end_term = min(prev_end_term, end)

        # return count