class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        rev_deg = 0
        for i in range(len(s)):
            normal_alb_position = ord(s[i]) - ord('a') + 1 # we add +1 because that difference start in 0 value
            rev_alb_position = 27 - normal_alb_position
            rev_deg += (i+1)*rev_alb_position

        return rev_deg