class Solution(object):
    def resultArray(self, nums, k, queries):
        n = len(nums)
        tree = [None] * (4 * n)

        def make_node(value):
            prod = value % k
            freq = [0] * k
            freq[prod] = 1
            return (prod, freq)

        def merge(left, right):
            left_prod, left_freq = left
            right_prod, right_freq = right

            prod = (left_prod * right_prod) % k
            freq = [0] * k

            for r in range(k):
                freq[r] += left_freq[r]

            for r in range(k):
                new_r = (left_prod * r) % k
                freq[new_r] += right_freq[r]

            return (prod, freq)

        def build(node, l, r):
            if l == r:
                tree[node] = make_node(nums[l])
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, index, value):
            if l == r:
                tree[node] = make_node(value)
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        result = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            node = query(1, 0, n - 1, start, n - 1)

            result.append(node[1][x])

        return result