class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        lst = []
        while n != 0:
            lst.append(n%10)
            n = n//10

        lst.sort(reverse = True)
        return lst[0]*lst[1]