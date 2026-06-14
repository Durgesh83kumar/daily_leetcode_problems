class Solution(object):
    def getLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 1

        for i in range(n):
            freq = {}
            count_freq = {}

            for j in range(i, n):
                x = nums[j]

                old = freq.get(x, 0)
                if(old>0):
                    count_freq[old] -= 1
                    if(count_freq[old] == 0):
                        del count_freq[old]


                new = old + 1
                freq[x] = new
                count_freq[new] = count_freq.get(new,0) + 1

                length = j - i + 1

                if(len(freq)==1):
                    ans = max(ans, length)

                elif (len(count_freq)==2):
                    f1, f2 = list(count_freq.keys())

                    if(f1>f2):
                        f1, f2 = f2, f1

                    if(f2 == 2 * f1):
                        ans = max(ans, length)

        return ans