class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        lst = []
        for i in range(m):
            if(i==0):
                lst.append("." * n)
            else:
                lst.append("#" * (n-1) + ".")

        return lst