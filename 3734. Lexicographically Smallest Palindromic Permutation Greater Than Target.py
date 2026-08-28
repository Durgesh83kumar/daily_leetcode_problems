class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        n = len(s)

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        odd = []
        for i in range(26):
            if cnt[i] % 2:
                odd.append(i)

        if len(odd) > 1:
            return ""

        half_cnt = [x // 2 for x in cnt]
        half_len = n // 2

        def build_pal(first, middle):
            left = ''.join(chr(x + ord('a')) for x in first)
            right = left[::-1]

            if n % 2:
                return left + chr(middle + ord('a')) + right
            else:
                return left + right

        best = None

        for pos in range(half_len - 1, -1, -1):
            available = half_cnt[:]
            first = []
            valid_prefix = True

            for j in range(pos):
                x = ord(target[j]) - ord('a')

                if available[x] == 0:
                    valid_prefix = False
                    break

                first.append(x)
                available[x] -= 1

            if not valid_prefix:
                continue

            target_x = ord(target[pos]) - ord('a')

            for x in range(target_x + 1, 26):
                if available[x] == 0:
                    continue

                temp = available[:]
                temp[x] -= 1

                suffix = []

                for c in range(26):
                    suffix.extend([c] * temp[c])

                candidate_first = first + [x] + suffix
                middle = odd[0] if n % 2 else -1
                candidate = build_pal(candidate_first, middle)

                if candidate > target:
                    if best is None or candidate < best:
                        best = candidate

                break

        available = half_cnt[:]
        first = []
        possible = True

        for i in range(half_len):
            x = ord(target[i]) - ord('a')

            if available[x] == 0:
                possible = False
                break

            first.append(x)
            available[x] -= 1

        if possible and sum(available) == 0:
            if n % 2:
                middle = odd[0]
                candidate = build_pal(first, middle)

                if candidate > target:
                    if best is None or candidate < best:
                        best = candidate
            else:
                candidate = build_pal(first, -1)

                if candidate > target:
                    if best is None or candidate < best:
                        best = candidate

        return best if best is not None else ""