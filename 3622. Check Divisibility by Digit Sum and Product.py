class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = n
        lst = []
        while num!=0:
            d = num%10
            lst.append(d)
            num = num//10

        total = 0
        product = 1
        for digit in lst:
            total += digit
            product *= digit
        
        res = total + product
        
        if (n%res) == 0:
            return True
        else:
            return False