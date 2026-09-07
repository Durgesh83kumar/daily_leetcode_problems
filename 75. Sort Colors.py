class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = 0
        c = 0

        for i in range(len(nums)):
            if nums[i]==0:
                a += 1
            elif nums[i]==1:
                b += 1
            else:
                c += 1
        j = 0
        while a != 0:
            nums[j] = 0
            a -= 1
            j += 1
        while b != 0:
            nums[j] = 1
            b -= 1
            j += 1
        while c != 0:
            nums[j] = 2
            c -= 1
            j += 1
        
        return nums

# Dutch national flag algorithm

        # low = 0
        # mid = 0
        # high = len(nums)-1

        # while mid<=high:
        #     if nums[mid] == 0:
        #         nums[mid], nums[low] = nums[low], nums[mid]
        #         mid += 1
        #         low += 1
        #     elif nums[mid] == 1:
        #         mid += 1
        #     else:
        #         nums[mid], nums[high] = nums[high], nums[mid]
        #         high -= 1

        # return nums