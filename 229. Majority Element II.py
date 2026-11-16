class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ## Optimal solution
        n = len(nums)
        count1, count2 = 0, 0
        elt1 = None
        elt2 = None

        for i in range(n):
            if count1 == 0 and nums[i] != elt2:
                count1 += 1
                elt1 = nums[i]
            elif count2 == 0 and nums[i] != elt1:
                count2 += 1
                elt2 = nums[i]
            elif elt1 == nums[i]:
                count1 += 1
            elif elt2 == nums[i]:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        lst = []
        count1, count2 = 0, 0
        for i in range(n):
            if elt1 == nums[i]:
                count1 += 1
            if elt2 == nums[i]:
                count2 += 1
        mini = n/3 + 1
        if count1 >= mini:
            lst.append(elt1)
        if count2 >= mini:
            lst.append(elt2)
        
        return lst
        

        # ## brute force approach
        # n = len(nums)
        # lst = []
        # for i in range(n):
        #     if not lst or lst[0] != nums[i]:
        #         count = 0
        #         for j in range(n):
        #             if nums[j] == nums[i]:
        #                 count += 1
        #         if count>n/3:
        #             lst.append(nums[i])
        #     if len(lst) == 2:
        #         break
        # return lst