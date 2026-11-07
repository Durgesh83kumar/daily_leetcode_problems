class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # # brute force approach
        # n = len(nums)
        # st = set()
        # for a in range(n):
        #     for b in range(a+1,n):
        #         for c in range(b+1, n):
        #             for d in range(c+1, n):
        #                 if nums[a]+nums[b]+nums[c]+nums[d] == target:
        #                     lst = [nums[a],nums[b],nums[c],nums[d]]
        #                     lst.sort()
        #                     st.add(tuple(lst))
        # ans = [list(t) for t in st]
        # return ans

        # # Optimal approach
        n = len(nums)
        ans = []
        nums.sort()
        for a in range(n):
            if(a>0 and nums[a]==nums[a-1]):
                continue
            for b in range(a+1,n):
                if (b>a+1 and a<b and nums[b]==nums[b-1]):
                    continue
                c = b+1
                d = n-1
                while(c<d):
                    sum = nums[a]+nums[b]+nums[c]+nums[d]
                    if sum<target:
                        c += 1
                    elif sum>target:
                        d -= 1
                    else:
                        ans.append([nums[a],nums[b],nums[c],nums[d]])
                        c += 1
                        d -= 1
                        while(c<d and nums[c]==nums[c-1]):
                            c += 1
                        while(c<d and nums[d]==nums[d+1]):
                            d -= 1
        return ans