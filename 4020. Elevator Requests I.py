class Solution(object):
    def elevatorRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[int]
        :rtype: int
        """
        f = 0
        total_time = 0
        i = 0
        while i<len(requests):
            if f != requests[i]:
                total_time += abs(f-requests[i])
                f = requests[i]
            i += 1
        return total_time