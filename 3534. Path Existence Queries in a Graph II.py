class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        arr = sorted((nums[i], i) for i in range(n))

        values = [x[0] for x in arr]
        node = [x[1] for x in arr]

        pos = [0] * n
        for i in range(n):
            pos[node[i]] = i

        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if values[i] - values[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        nextPos = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and values[j + 1] - values[i] <= maxDiff:
                j += 1
            nextPos[i] = j

        LOG = n.bit_length()

        up = [nextPos]

        for _ in range(1, LOG):
            prev = up[-1]
            curr = [0] * n
            for i in range(n):
                curr[i] = prev[prev[i]]
            up.append(curr)

        ans = []

        for u, v in queries:

            if u == v:
                ans.append(0)
                continue

            su = pos[u]
            sv = pos[v]

            if comp[su] != comp[sv]:
                ans.append(-1)
                continue

            if su > sv:
                su, sv = sv, su

            cur = su
            jumps = 0

            for k in range(LOG - 1, -1, -1):
                nxt = up[k][cur]
                if nxt < sv:
                    cur = nxt
                    jumps += 1 << k

            ans.append(jumps + 1)

        return ans