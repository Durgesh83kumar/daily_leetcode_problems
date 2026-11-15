class Solution(object):
    def numOfSubarrays(self, arr):
        """:type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1
        current_sum = 0
        result = 0
        
        for num in arr:
            current_sum += num
            
            if current_sum % 2 == 1:
                result = (result + even_count) % MOD
                odd_count += 1
            else:
                result = (result + odd_count) % MOD
                even_count += 1
                
        return result