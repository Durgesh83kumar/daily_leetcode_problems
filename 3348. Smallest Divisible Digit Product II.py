class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        n = len(num)

        e2 = e3 = e5 = e7 = 0
        tt = t
        while tt % 2 == 0:
            e2 += 1; tt //= 2
        while tt % 3 == 0:
            e3 += 1; tt //= 3
        while tt % 5 == 0:
            e5 += 1; tt //= 5
        while tt % 7 == 0:
            e7 += 1; tt //= 7
        if tt != 1:
            return "-1"

        E2, E3, E5, E7 = e2, e3, e5, e7

        EXP2 = [0,0,1,0,2,0,1,0,3,0]
        EXP3 = [0,0,0,1,0,0,1,0,0,2]
        EXP5 = [0,0,0,0,0,1,0,0,0,0]
        EXP7 = [0,0,0,0,0,0,0,1,0,0]

        maxA, maxB = E2 + 1, E3 + 1
        INF = float('inf')
        dp = [[0]*maxB for _ in range(maxA)]
        combo_digits = [2,3,4,6,8,9] 

        for a in range(maxA):
            for b in range(maxB):
                if a == 0 and b == 0:
                    dp[a][b] = 0
                    continue
                best = INF
                for d in combo_digits:
                    da, db = EXP2[d], EXP3[d]
                    na, nb = max(0, a-da), max(0, b-db)
                    if na == a and nb == b:
                        continue
                    cand = 1 + dp[na][nb]
                    if cand < best:
                        best = cand
                dp[a][b] = best

        def minCount(a, b):
            a = 0 if a < 0 else min(a, maxA-1)
            b = 0 if b < 0 else min(b, maxB-1)
            return dp[a][b]

        def feasible(r2, r3, r5, r7, L):
            if r5 + r7 > L:
                return False
            rem = L - r5 - r7
            return minCount(r2, r3) <= rem

        def build(L, r2, r3, r5, r7):
            res = []
            for pos in range(L):
                rem_after = L - pos - 1
                for d in range(1, 10):
                    nr2 = max(0, r2-EXP2[d]); nr3 = max(0, r3-EXP3[d])
                    nr5 = max(0, r5-EXP5[d]); nr7 = max(0, r7-EXP7[d])
                    if feasible(nr2, nr3, nr5, nr7, rem_after):
                        res.append(str(d))
                        r2, r3, r5, r7 = nr2, nr3, nr5, nr7
                        break
            return ''.join(res)

        if '0' not in num:
            pe2 = pe3 = pe5 = pe7 = 0
            for ch in num:
                d = int(ch)
                pe2 = min(E2, pe2+EXP2[d]); pe3 = min(E3, pe3+EXP3[d])
                pe5 = min(E5, pe5+EXP5[d]); pe7 = min(E7, pe7+EXP7[d])
            if pe2 >= E2 and pe3 >= E3 and pe5 >= E5 and pe7 >= E7:
                return num

        prefE2 = [0]*(n+1); prefE3 = [0]*(n+1)
        prefE5 = [0]*(n+1); prefE7 = [0]*(n+1)
        for k in range(n):
            d = int(num[k])
            prefE2[k+1] = min(E2, prefE2[k]+EXP2[d])
            prefE3[k+1] = min(E3, prefE3[k]+EXP3[d])
            prefE5[k+1] = min(E5, prefE5[k]+EXP5[d])
            prefE7[k+1] = min(E7, prefE7[k]+EXP7[d])

        zero_idx = num.find('0')
        start = zero_idx if zero_idx != -1 else n-1

        for i in range(start, -1, -1):
            r2 = E2 - prefE2[i]; r3 = E3 - prefE3[i]
            r5 = E5 - prefE5[i]; r7 = E7 - prefE7[i]
            L = n - 1 - i
            orig_d = int(num[i])
            for d in range(orig_d+1, 10):
                nr2 = max(0, r2-EXP2[d]); nr3 = max(0, r3-EXP3[d])
                nr5 = max(0, r5-EXP5[d]); nr7 = max(0, r7-EXP7[d])
                if feasible(nr2, nr3, nr5, nr7, L):
                    suffix = build(L, nr2, nr3, nr5, nr7)
                    return num[:i] + str(d) + suffix

        Lmin_full = E5 + E7 + minCount(E2, E3)
        target = max(n+1, Lmin_full)
        return build(target, E2, E3, E5, E7)