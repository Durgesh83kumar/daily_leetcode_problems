class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """

        n = len(s)

        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for i in range(n - 1, -1, -1):

            cnt = count[:]

            possible = True

            for j in range(i):
                x = ord(target[j]) - ord('a')

                if cnt[x] == 0:
                    possible = False
                    break

                cnt[x] -= 1

            if not possible:
                continue

            x = ord(target[i]) - ord('a')

            for c in range(x + 1, 26):
                if cnt[c] > 0:

                    cnt[c] -= 1

                    ans = target[:i] + chr(c + ord('a'))

                    for k in range(26):
                        ans += chr(k + ord('a')) * cnt[k]

                    return ans

        return ""
        