class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1:
            return 1
    
        maxi = max(nums)
        mini = min(nums)

        d = []
        for i in range(n):
            if nums[i]==maxi:
                d.append(i+1)
            if nums[i]==mini:
                d.append(i+1)
        
        a = max(d) # Both from front
        b = n-min(d)+1 # Both from back
        c = min(d) + n - max(d) + 1 # Remove one from each side

        return min(a,b,c)