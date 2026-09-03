class Solution(object):
    def uniformArray(self, nums1):
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x % 2 == 0:
                min_even = min(min_even, x)
            else:
                min_odd = min(min_odd, x)

        possible_odd = True

        for x in nums1:
            if x % 2 == 0:

                if min_odd >= x:
                    possible_odd = False
                    break

        if possible_odd:
            return True

        possible_even = True

        for x in nums1:
            if x % 2 == 1:
 
                if min_odd >= x:
                    possible_even = False
                    break

        return possible_even