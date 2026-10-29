class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length()
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = u if p == -1 else p
                if p != -1:
                    depth[u] = depth[p] + 1

                tin[u] = timer
                timer += 1

                stack.append((u, p, 1))

                for v in reversed(adj[u]):
                    if v != p:
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        up = [[0] * n for _ in range(LOG)]
        up[0] = parent[:]

        for j in range(1, LOG):
            for u in range(n):
                up[j][u] = up[j - 1][up[j - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0

            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        bit = [0] * (n + 2)

        def add(i, val):
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def range_xor(left, right, val):
            add(left + 1, val)
            add(right + 1, val)

        def point_query(pos):
            res = 0
            pos += 1

            while pos > 0:
                res ^= bit[pos]
                pos -= pos & -pos

            return res

        chars = [1 << (ord(c) - ord('a')) for c in s]

        for u in range(n):
            range_xor(tin[u], tout[u], chars[u])

        ans = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - ord('a'))
                delta = chars[u] ^ new_mask

                if delta:
                    range_xor(tin[u], tout[u], delta)
                    chars[u] = new_mask

            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)

                mask = (
                    point_query(tin[u])
                    ^ point_query(tin[v])
                    ^ chars[w]
                )

                ans.append((mask & (mask - 1)) == 0)

        return ans