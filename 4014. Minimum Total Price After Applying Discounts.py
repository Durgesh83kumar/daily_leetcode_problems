class Solution(object):
    def minPrice(self, prices, discounts):
        """
        :type prices: List[int]
        :type discounts: List[int]
        :rtype: float
        """
        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        result = 0.0

        for i in range(min(len(prices),len(discounts))):
            result += (prices[i] * (100 - discounts[i])) / 100.0

        if len(prices) > len(discounts):

            for i in range(len(discounts), len(prices)):
                result += prices[i]

        return result