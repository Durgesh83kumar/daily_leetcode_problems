class Solution(object):
    def checkGoodInteger(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = str(n)
        digitSum = 0
        squareSum = 0
        for i in range(len(s)):
            digitSum += int(s[i])
            squareSum += (int(s[i]))**2
        if(squareSum - digitSum)>= 50:
            return True
        else:
            return False