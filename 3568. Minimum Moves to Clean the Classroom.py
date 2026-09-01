from collections import deque

class Solution(object):

    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """

        m = len(classroom)
        n = len(classroom[0])

        start_r = start_c = -1
        litter = {}

        count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c

                elif classroom[r][c] == 'L':
                    litter[(r, c)] = count
                    count += 1

        if count == 0:
            return 0

        target = (1 << count) - 1

        q = deque()
        q.append((start_r, start_c, 0, energy, 0))

        best = {}

        best[(start_r, start_c, 0)] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:

            r, c, mask, curr_energy, moves = q.popleft()

            if mask == target:
                return moves

            if curr_energy == 0:
                continue

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                new_energy = curr_energy - 1

                new_mask = mask

                if classroom[nr][nc] == 'L':
                    idx = litter[(nr, nc)]
                    new_mask |= (1 << idx)

                if classroom[nr][nc] == 'R':
                    new_energy = energy

                state = (nr, nc, new_mask)

                if state in best and best[state] >= new_energy:
                    continue

                best[state] = new_energy

                q.append(
                    (nr, nc, new_mask, new_energy, moves + 1)
                )

        return -1