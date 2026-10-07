class Solution(object):
    def removeInvalidParentheses(self, s):
        queue = {s}
        visited = {s}
        ans = []

        while queue:
            for cur in queue:
                if self.isValid(cur):
                    ans.append(cur)

            if ans:
                return list(set(ans))

            next_queue = set()

            for cur in queue:
                for i in range(len(cur)):
                    if cur[i] not in "()":
                        continue

                    new_s = cur[:i] + cur[i + 1:]

                    if new_s not in visited:
                        visited.add(new_s)
                        next_queue.add(new_s)

            queue = next_queue

        return [""]

    def isValid(self, s):
        balance = 0

        for ch in s:
            if ch == '(':
                balance += 1

            elif ch == ')':
                balance -= 1

                if balance < 0:
                    return False

        return balance == 0
        