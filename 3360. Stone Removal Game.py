class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = 10
        count = 0
        while n>=temp:
            n = n - temp
            temp = temp - 1
            count = count + 1
        if count % 2 == 0:
            return False
        else:
            return True


        # temp = 10
        # count = 0
        # while n>=0:
        #     n = n - temp
        #     temp = temp - 1
        #     count += 1
        # if count % 2 == 0:
        #     return True
        # else:
        #     return False