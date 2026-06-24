class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """ 
        d = {5:0, 10:0}
        for i in range(0, len(bills)):
            if bills[i] == 5:
                d[bills[i]] += 1

            elif bills[i] == 10:
                if d[5] == 0:
                    return False
                d[bills[i]] += 1
                d[5] -= 1

            elif bills[i] == 20:
                if d[10]>0 and d[5]>0:
                    d[10] -= 1
                    d[5] -= 1
                elif d[5]>=3:
                    d[5] -= 3
                else:
                    return False

        return True