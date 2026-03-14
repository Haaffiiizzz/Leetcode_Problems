class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness_up_to(x: int) -> int:
            if x <= 0:
                return 0

            s = str(x)
            n = len(s)

            from functools import lru_cache

            @lru_cache(None)
            def dp(pos: int, tight: bool, started: bool, prev1: int, prev2: int):
                """
                Returns (count_numbers, total_wavy_positions) for suffix starting at pos.
                prev2 = digit at pos-2, prev1 = digit at pos-1; 10 denotes "no digit yet".
                """
                if pos == n:
                    return (1, 0) if started else (0, 0)

                limit = int(s[pos]) if tight else 9
                total_count = 0
                total_wavy = 0

                for d in range(0, limit + 1):
                    next_tight = tight and (d == limit)
                    if not started:
                        # Still skipping leading zeros
                        if d == 0:
                            cnt, wvy = dp(pos + 1, next_tight, False, 10, 10)
                            total_count += cnt
                            total_wavy += wvy
                            continue
                        # Starting the number with first non-zero digit
                        cnt, wvy = dp(pos + 1, next_tight, True, d, 10)
                        total_count += cnt
                        total_wavy += wvy
                        continue

                    # started == True
                    add = 0
                    if prev2 != 10:
                        if (prev1 > prev2 and prev1 > d) or (prev1 < prev2 and prev1 < d):
                            add = 1

                    cnt, wvy = dp(pos + 1, next_tight, True, d, prev1)
                    total_count += cnt
                    total_wavy += wvy + add * cnt

                return total_count, total_wavy

            return dp(0, True, False, 10, 10)[1]

        return waviness_up_to(num2) - waviness_up_to(num1 - 1)