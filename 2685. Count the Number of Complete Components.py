class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            vertices = 1
            edge_count = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    v, e = dfs(nei)
                    vertices += v
                    edge_count += e

            return vertices, edge_count

        for i in range(n):
            if not visited[i]:
                vertices, edge_count = dfs(i)
                edge_count //= 2

                if edge_count == vertices * (vertices - 1) // 2:
                    ans += 1

        return ans