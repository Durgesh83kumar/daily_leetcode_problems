class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        n = len(items)
        freq = [0] * (n + 1)
        min_price = None

        for factor, price in items:
            freq[factor] += 1
            if min_price is None or price < min_price:
                min_price = price

        mult_count = [0] * (n + 1)
        for f in xrange(1, n + 1):
            total = 0
            for m in xrange(f, n + 1, f):
                total += freq[m]
            mult_count[f] = total

        candidates = []
        for factor, price in items:
            gain = mult_count[factor] - 1
            candidates.append((price, gain))

        candidates.sort(key=lambda x: x[0])

        best = budget // min_price
        spent = 0
        gained = 0

        for price, gain in candidates:
            if gain <= 0 or spent >= budget:
                continue

            max_take = gain
            rem_budget = budget - spent
            if rem_budget // price < max_take:
                max_take = rem_budget // price

            if max_take > 0:
                spent += max_take * price
                gained += 2 * max_take
                total_items = gained + ((budget - spent) // min_price)
                if total_items > best:
                    best = total_items

        return best