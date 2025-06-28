from math import inf

class Solution:
    def minXor(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # Precompute prefix XOR so subarray XOR can be computed in O(1)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] ^ nums[i]
        
        # dp[i][j] will be the minimal possible maximum XOR when partitioning
        # the first i elements into j segments.
        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # Base case: zero elements, 0 segments
        
        for i in range(n):
            for parts in range(k):
                if dp[i][parts] < inf:
                    # Try all possible next split points
                    for j in range(i + 1, n + 1):
                        # XOR of nums[i:j]
                        seg_xor = prefix[j] ^ prefix[i]
                        # The maximum XOR for this partitioning option
                        curr_max = max(dp[i][parts], seg_xor)
                        dp[j][parts + 1] = min(dp[j][parts + 1], curr_max)
        
        return dp[n][k]
