class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        a1 = (ax2 - ax1)*(ay2 - ay1)
        a2 = (bx2 - bx1)*(by2 - by1)

        overlap_width = max(0, min(ax2,bx2)-max(ax1,bx1))
        overlap_height = max(0, min(ay2,by2)-max(ay1,by1))

        overlap = overlap_width*overlap_height
        
        return a1 + a2 - overlap