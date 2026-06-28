class Solution(object):
    def filterOccupiedIntervals(self, occupiedIntervals, freeStart, freeEnd):
        """
        :type occupiedIntervals: List[List[int]]
        :type freeStart: int
        :type freeEnd: int
        :rtype: List[List[int]]
        """
        if not occupiedIntervals:
            return[]

        occupiedIntervals.sort()

        merged = []

        for s, e in occupiedIntervals:
            if not merged or s > merged[-1][1] + 1:
                merged.append([s,e])
            else:
                merged[-1][1] = max(merged[-1][1], e)


        ans = []

        for s, e in merged:
            if e < freeStart or s > freeEnd:
                ans.append([s,e])
            else:
                if s < freeStart:
                    ans.append([s,freeStart -1])
                
                if e > freeEnd:
                    ans.append([freeEnd + 1, e])

        return ans