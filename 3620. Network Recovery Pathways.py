from collections import deque

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        costs = set()

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            costs.add(w)

        # Topological order of original DAG
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        vals = sorted(costs)

        INF = float('inf')

        def check(limit):
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                # intermediate offline nodes cannot be used
                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:
                    if w < limit:
                        continue
                    if v != n - 1 and v != 0 and not online[v]:
                        continue
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

            return dist[n - 1] <= k

        if not vals:
            return -1

        # No valid path even without restriction
        if not check(0):
            return -1

        lo, hi = 0, len(vals) - 1
        ans = vals[0]

        while lo <= hi:
            mid = (lo + hi) // 2
            if check(vals[mid]):
                ans = vals[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans