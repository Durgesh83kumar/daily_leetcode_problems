class Solution(object):
    def nearestDrone(self, drones, target):
        """
        :type drones: List[List[int]]
        :type target: List[int]
        :rtype: int
        """
        b = -1
        b_d = float("inf")

        for i, (x, y, r) in enumerate(drones):
            ds = abs(x - target[0]) + abs(y - target[1])

            if ds <= r and ds < b_d:
                b_d = ds
                b = i

        return b