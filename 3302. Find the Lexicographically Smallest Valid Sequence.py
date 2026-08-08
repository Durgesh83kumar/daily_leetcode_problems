class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """

        n = len(word1)
        m = len(word2)

        suf = [-1] * m

        j = n - 1

        for i in range(m - 1, -1, -1):
            while j >= 0 and word1[j] != word2[i]:
                j -= 1

            if j < 0:
                break

            suf[i] = j
            j -= 1

        ans = []
        j = 0
        mismatch = False

        for i in range(m):

            while j < n:

                if word1[j] == word2[i]:
                    ans.append(j)
                    j += 1
                    break

                if not mismatch:
                    if i == m - 1 or (
                        suf[i + 1] != -1 and suf[i + 1] > j
                    ):
                        ans.append(j)
                        mismatch = True
                        j += 1
                        break

                j += 1

            else:
                return []

        return ans
        