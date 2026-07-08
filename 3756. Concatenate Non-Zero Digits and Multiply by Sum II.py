class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        n = len(s)

        digits = []
        pos = []

        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))
                pos.append(i)

        m = len(digits)

        if m == 0:
            return [0] * len(queries)

        prefSum = [0] * (m + 1)
        for i in range(m):
            prefSum[i + 1] = prefSum[i] + digits[i]

        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        prefNum = [0] * (m + 1)
        for i in range(m):
            prefNum[i + 1] = (prefNum[i] * 10 + digits[i]) % MOD

        nextIdx = [-1] * n
        prevIdx = [-1] * n

        p = 0
        for i in range(n):
            while p < m and pos[p] < i:
                p += 1
            if p < m:
                nextIdx[i] = p

        p = m - 1
        for i in range(n - 1, -1, -1):
            while p >= 0 and pos[p] > i:
                p -= 1
            if p >= 0:
                prevIdx[i] = p

        ans = []

        for l, r in queries:
            L = nextIdx[l]
            R = prevIdx[r]

            if L == -1 or R == -1 or L > R:
                ans.append(0)
                continue

            length = R - L + 1

            x = (prefNum[R + 1] - prefNum[L] * pow10[length]) % MOD
            digitSum = prefSum[R + 1] - prefSum[L]

            ans.append((x * digitSum) % MOD)

        return ans