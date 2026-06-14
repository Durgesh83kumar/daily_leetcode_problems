class Solution(object):
    def maxRatings(self, units):
        """
        :type units: List[List[int]]
        :rtype: int
        """
        m = len(units)
        n = len(units[0])

        if(n==1):
            return sum(row[0] for row in units)

        total = 0
        smallest_second = float("inf")
        smallest_all = float("inf")

        for row in units:
            row.sort()

            smallest_all = min(smallest_all, row[0])
            total += row[1]
            smallest_second = min(smallest_second, row[1])

        return total - smallest_second + smallest_all