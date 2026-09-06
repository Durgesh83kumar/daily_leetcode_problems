class Solution(object):
    def countGoodRotations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        half = n//2
        arr = nums + nums
        first_sum = sum(arr[0:half])
        second_sum = sum(arr[half:n])

        good_count = 0
        if first_sum > second_sum:
            good_count += 1

        for i in range(1,n):
            first_sum += arr[i+half-1]-arr[i-1]
            second_sum += arr[i + n - 1] - arr[i+half-1]

            if first_sum>second_sum:
                good_count += 1

        return good_count