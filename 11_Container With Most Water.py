class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i = 0
        j = len(height)-1
        while(i<j):
            ll = height[i]
            rl = height[j]
            if(ll>rl):
                area = rl*(j-i)
                j = j - 1
            else:
                area = ll*(j-i)
                i = i + 1

            if(max_area < area):
                max_area = area

        return max_area