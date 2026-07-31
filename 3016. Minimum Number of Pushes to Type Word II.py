from collections import Counter

class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq = Counter(word)

        # Frequencies in descending order
        counts = sorted(freq.values(), reverse=True)

        answer = 0

        for i, f in enumerate(counts):
            pushes = i // 8 + 1
            answer += f * pushes

        return answer