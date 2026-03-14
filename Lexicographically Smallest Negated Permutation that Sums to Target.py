from typing import List


class Solution:
    def constructPermutation(self, n: int, target: int) -> List[int]:
        """
        Return lexicographically smallest length-n array whose absolute values are
        1..n and whose sum equals target. If impossible, return [].
        """
        total = n * (n + 1) // 2
        if abs(target) > total or ((total - target) & 1):
            return []


        from functools import lru_cache

        @lru_cache(None)
        def can(mask: int, rem: int) -> bool:
            """Feasibility of reaching 'rem' using unused numbers in mask."""
            if mask == 0:
                return rem == 0
            # Quick bound pruning
            max_abs = 0
            tmp = mask
            bit = 1
            while tmp:
                if tmp & 1:
                    max_abs += bit
                tmp >>= 1
                bit += 1
            if rem < -max_abs or rem > max_abs:
                return False

            # Try each available number with both signs
            for a in range(1, n + 1):
                bitmask = 1 << (a - 1)
                if not (mask & bitmask):
                    continue
                next_mask = mask ^ bitmask
                if can(next_mask, rem - a) or can(next_mask, rem + a):
                    return True
            return False

        mask_all = (1 << n) - 1
        result = []
        rem = target

        while mask_all:
            chosen = None
            # Order candidates by signed value: negative large to small, then positive small to large
            for sign in (-1, 1):
                if sign == -1:
                    abs_iter = range(n, 0, -1)
                else:
                    abs_iter = range(1, n + 1)
                for a in abs_iter:
                    bitmask = 1 << (a - 1)
                    if not (mask_all & bitmask):
                        continue
                    val = sign * a
                    next_mask = mask_all ^ bitmask
                    if can(next_mask, rem - val):
                        chosen = (val, next_mask)
                        break
                if chosen:
                    break

            if chosen is None:
                return []

            val, mask_all = chosen
            result.append(val)
            rem -= val

        return result
