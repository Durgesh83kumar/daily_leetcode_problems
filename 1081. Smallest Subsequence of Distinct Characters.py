class Solution(object):
    def smallestSubsequence(self, s):
        last = {}

        # Store the last index of each character
        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        seen = set()

        for i, ch in enumerate(s):

            # Skip if already included
            if ch in seen:
                continue

            # Remove larger characters if they appear again later
            while (stack and
                   stack[-1] > ch and
                   last[stack[-1]] > i):

                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)