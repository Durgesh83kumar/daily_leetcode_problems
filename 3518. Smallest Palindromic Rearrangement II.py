from collections import Counter
def comb(n, r):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    ans = 1
    for i in range(1, r + 1):
        ans = ans * (n - r + i) // i
    return ans

class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        LIMIT = 10**6 + 1

        freq = Counter(s)

        mid = ""
        half = {}

        total_half = 0
        for ch in sorted(freq):
            if freq[ch] % 2:
                mid = ch
            half[ch] = freq[ch] // 2
            total_half += half[ch]

        def count_perm(cnt):
            rem = sum(cnt.values())
            ans = 1
            for c in cnt.values():
                if c:
                    ans *= comb(rem, c)
                    if ans > LIMIT:
                        return LIMIT
                    rem -= c
            return ans

        if count_perm(half) < k:
            return ""

        first = []

        for _ in range(total_half):
            for ch in sorted(half):
                if half[ch] == 0:
                    continue

                half[ch] -= 1
                ways = count_perm(half)

                if ways >= k:
                    first.append(ch)
                    break
                else:
                    k -= ways
                    half[ch] += 1

        first = "".join(first)
        return first + mid + first[::-1]
        