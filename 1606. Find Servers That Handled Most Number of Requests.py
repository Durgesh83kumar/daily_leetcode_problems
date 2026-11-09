import heapq
from sortedcontainers import SortedList

class Solution(object):
    def busiestServers(self, k, arrival, load):
        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            start = arrival[i]

            while busy and busy[0][0] <= start:
                end_time, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            idx = available.bisect_left(i % k)

            if idx == len(available):
                idx = 0

            server = available.pop(idx)

            count[server] += 1
            heapq.heappush(busy, (start + load[i], server))

        max_count = max(count)

        return [i for i in range(k) if count[i] == max_count]