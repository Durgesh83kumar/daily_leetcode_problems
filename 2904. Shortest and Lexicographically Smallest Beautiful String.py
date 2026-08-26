class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = [] 
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substring = s[i:j]

                if substring.count("1")==k:
                    ans.append(substring)

        if ans:
            smallest = ans[0]
            for r in range(1,len(ans)):
                if len(ans[r])<len(smallest):
                    smallest = ans[r]
                elif len(ans[r])==len(smallest):
                    smallest = min(ans[r],smallest)
            return smallest
        return ""