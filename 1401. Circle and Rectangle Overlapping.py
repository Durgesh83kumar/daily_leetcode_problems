class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        
        px = max(x1, min(xCenter, x2))
        py = max(y1, min(yCenter, y2))

        distance_squared = (px - xCenter) ** 2 + (py - yCenter) ** 2

        return distance_squared <= radius ** 2