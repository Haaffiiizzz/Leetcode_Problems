class Solution:
    def minFlips(self, n: int) -> int:
        """
        Minimum flips to make the binary string of n equal to its reverse.

        Only mirrored positions i and j = len(s) - 1 - i matter. If they differ,
        both sides need one flip, so each mismatch adds 2 flips total.
        """
        s = bin(n)[2:]  # strip "0b" prefix
        half = len(s) // 2

        mismatches = 0
        for i in range(half):
            if s[i] != s[-1 - i]:
                mismatches += 1

        return mismatches * 2
