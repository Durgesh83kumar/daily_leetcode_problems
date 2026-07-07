class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        x = ""
        while(n>=1):
            last_digit = n%10
            n = n//10
            if last_digit > 0:
                x = x + str(last_digit)
        
        total = 0
        x = x[::-1] # or x = "".join(reversed(x))
        for i in range(len(x)):
            total = total + int(x[i])

        return int(x) * total