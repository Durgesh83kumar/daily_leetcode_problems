
class Solution(object):
    def reversePairs(self, nums):

        def merge(arr, low, mid, high):
            left = low
            right = mid + 1
            ans = []

            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    ans.append(arr[left])
                    left += 1
                else:
                    ans.append(arr[right])
                    right += 1

            while left <= mid:
                ans.append(arr[left])
                left += 1

            while right <= high:
                ans.append(arr[right])
                right += 1

            arr[low:high+1] = ans

        def countPairs(arr, low, mid, high):
            right = mid + 1
            count = 0

            for i in range(low, mid+1):
                while right <= high and arr[i] > 2 * arr[right]:
                    right += 1

                count += right - (mid + 1)

            return count

        def mergeSortHelper(arr, low, high):
            count = 0

            if low >= high:
                return count

            mid = (low + high) // 2

            count += mergeSortHelper(arr, low, mid)
            count += mergeSortHelper(arr, mid+1, high)

            count += countPairs(arr, low, mid, high)

            merge(arr, low, mid, high)

            return count

        return mergeSortHelper(nums, 0, len(nums)-1)

            ## brute force approach
            
            # ans = 0
            # for i in range(len(nums)-1):
            #     for j in range(i+1,len(nums)):
            #         if nums[i]>2*nums[j]:
            #             ans += 1
            # return ans