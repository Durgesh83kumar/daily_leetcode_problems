from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        arr = []

        for i, interval in enumerate(intervals):
            l, r, w = interval
            arr.append((l, r, w, i))

        arr.sort(key=lambda x: x[1])

        rights = [x[1] for x in arr]

        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):
            for i in range(1, n + 1):

                not_take = dp[k][i - 1]

                l, r, w, original_index = arr[i - 1]

                j = bisect_left(rights, l) - 1

                previous_score, previous_indices = dp[k - 1][j + 1]

                candidate_score = previous_score + w
                candidate_indices = tuple(
                    sorted(previous_indices + (original_index,))
                )

                take = (candidate_score, candidate_indices)

                if take[0] > not_take[0]:
                    dp[k][i] = take

                elif take[0] < not_take[0]:
                    dp[k][i] = not_take

                else:

                    dp[k][i] = min(take, not_take)

        return list(dp[4][n][1])