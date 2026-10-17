class Solution(object):
    def minSwaps(self, nums):
        def digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        n = len(nums)
        target = sorted(nums, key=lambda x: (digit_sum(x), x))
        index = {num: i for i, num in enumerate(nums)}
        swaps = 0

        for i in range(n):
            while nums[i] != target[i]:
                j = index[target[i]]
                index[nums[i]] = j
                index[nums[j]] = i
                nums[i], nums[j] = nums[j], nums[i]
                swaps += 1

        return swaps