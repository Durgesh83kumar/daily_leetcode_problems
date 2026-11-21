class Solution(object):
    def findSubtreeSizes(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: List[int]
        """
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        new_parent = list(parent)
        last_seen = [-1] * 26

        def find_new_parents(u):
            idx = ord(s[u]) - ord('a')
            if last_seen[idx] != -1:
                new_parent[u] = last_seen[idx]

            prev = last_seen[idx]
            last_seen[idx] = u

            for v in adj[u]:
                find_new_parents(v)

            last_seen[idx] = prev

        find_new_parents(0)

        new_adj = [[] for _ in range(n)]
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)

        ans = [0] * n

        def calc_subtree_size(u):
            total = 1
            for v in new_adj[u]:
                total += calc_subtree_size(v)
            ans[u] = total
            return total

        calc_subtree_size(0)
        return ans