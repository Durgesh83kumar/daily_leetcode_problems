class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def backtrack(current,open_used, close_used):
            if(len(current)==2*n):
                res.append(current)
                return
            if(open_used<n):
                backtrack(current + "(",open_used+1,close_used)

            if(close_used<open_used):
                backtrack(current + ")",open_used,close_used+1)

        backtrack("", 0, 0)
        return res
            