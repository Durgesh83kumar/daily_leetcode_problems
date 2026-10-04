class Solution(object):
    def minRotations(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = 0
        min_rotation=0
        for d in s:
            digit = int(d)
            min_rotation += (digit-p)%10
            if(digit-p)%10>5:
                min_rotation -= 2*((digit-p)%10 - 5)

            p = digit

        return min_rotation