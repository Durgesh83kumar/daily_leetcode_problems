class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # # brute force approach

        # # n = len(nums)
        # # st = set()
        # # for i in range(n):
        # #     for j in range(i+1, n):
        # #         for k in range(j+1,n):
        # #             if nums[i]+nums[j]+nums[k] == 0:
        # #                 arr = [nums[i],nums[j],nums[k]]
        # #                 arr.sort()
        # #                 st.add(tuple(arr))
        # # ans = [list(t) for t in st]
        # # return ans

        # # better approach

        # n = len(nums)
        # st = set()
        # for i in range(n):
        #     hashset = set()
        #     for j in range(i+1,n):
        #         third_elt = -(nums[i]+nums[j])
        #         if third_elt in hashset:
        #             arr = [nums[i], nums[j], third_elt]
        #             arr.sort()
        #             st.add(tuple(arr))
        #         hashset.add(nums[j])
        # ans = [list(t) for t in st]
        # return ans

        # # Optimal approach
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n):
            if (i>0 and nums[i] == nums[i-1]):
                continue
            j = i + 1
            k = n - 1
            while(j<k):
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while(j<k and nums[j]==nums[j-1]):
                        j += 1
                    while(j<k and nums[k]==nums[k+1]):
                        k -= 1
        return ans