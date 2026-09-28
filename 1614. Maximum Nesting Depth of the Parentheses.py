class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        left_brackets = 0
        max_n_nes_par = 0
        for i in range(len(s)):
            if s[i]=="(":
                left_brackets += 1
                max_n_nes_par = max(max_n_nes_par, left_brackets)
            if s[i]==")":
                left_brackets -= 1
                max_n_nes_par = max(max_n_nes_par, left_brackets)


        return max_n_nes_par