class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def product_of_digit(n):

            p = 1
            while n != 0:
                d = n%10
                if d==0:
                    return 0
                
                p *= d
                n = n//10
            
            return p

        current = n
        while True:
            product = product_of_digit(current)

            if product % t == 0:
                return current
            
            current += 1