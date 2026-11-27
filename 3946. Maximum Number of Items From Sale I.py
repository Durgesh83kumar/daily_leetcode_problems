class Solution(object):
    def maximumSaleItems(self, items, budget):
        n = len(items)
        free_cnt = [0] * n

        for i in xrange(n):
            fi = items[i][0]
            cnt = 0
            for j in xrange(n):
                if i != j and items[j][0] % fi == 0:
                    cnt += 1
            free_cnt[i] = cnt

        dp = [0] * (budget + 1)

        for i in xrange(n):
            price = items[i][1]
            if price > budget:
                continue

            gain_first = 1 + free_cnt[i]
            for b in xrange(budget, price - 1, -1):
                if dp[b - price] + gain_first > dp[b]:
                    dp[b] = dp[b - price] + gain_first

            for b in xrange(price, budget + 1):
                if dp[b - price] + 1 > dp[b]:
                    dp[b] = dp[b - price] + 1

        return dp[budget]