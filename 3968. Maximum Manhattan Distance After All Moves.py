class Solution(object):
    def maxDistance(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        ans = 0
        directions = [
            ('R','U'),
            ('R','D'),
            ('L','U'),
            ('L','D')
        ]
        for a, b in directions:
            total = 0
            for ch in moves:
                if(ch==a or ch==b or ch=='_'):
                    total += 1
                else:
                    total -= 1
            ans = max(ans, abs(total))
        return ans