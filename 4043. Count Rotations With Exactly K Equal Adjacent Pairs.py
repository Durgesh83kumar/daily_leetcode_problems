class Solution(object):
    def countRotations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(s)
        for i in range(n):
            r_s = s[i:]+s[:i]
            score = 0
            for j in range(n-1):
                if r_s[j] == r_s[j+1]:
                    score += 1
            if score == k:
                count += 1
        return count