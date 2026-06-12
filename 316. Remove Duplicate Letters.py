class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_index = {}
        for i, ch in enumerate(s):
            last_index[ch] = i

        stack = []
        visited = set()

        for i, ch in enumerate(s):
            if(ch in visited):
                continue
            
            while(stack and ch < stack[-1] and last_index[stack[-1]]>i):
                removed = stack.pop()
                visited.remove(removed)
            
            stack.append(ch)
            visited.add(ch)

        return "".join(stack)

        