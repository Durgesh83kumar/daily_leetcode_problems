class Solution(object):
    def findKthSmallest(self, coins, k):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a // gcd(a, b) * b

        coins.sort()

        # Remove redundant coins
        filtered = []

        for c in coins:
            redundant = False

            for x in filtered:
                if c % x == 0:
                    redundant = True
                    break

            if not redundant:
                filtered.append(c)

        coins = filtered
        n = len(coins)

        def count(x):
            total = 0

            for mask in range(1, 1 << n):

                multiple = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        multiple = lcm(multiple, coins[i])

                        if multiple > x:
                            break

                else:
                    value = x // multiple

                    if bits % 2 == 1:
                        total += value
                    else:
                        total -= value

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left