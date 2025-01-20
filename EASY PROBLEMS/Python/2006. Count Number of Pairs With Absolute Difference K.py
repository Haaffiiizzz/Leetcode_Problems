class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        pairs = 0
        pairsDict = {}

        for i in nums:
            pair = (i - k, i + k)
            if  i in pairsDict:
                pairsDict[i][1] += 1
            else:
                pairsDict[i] = [pair, 1]
            for num in pair:
                if num in pairsDict:
                    pairs += pairsDict[num][1]
        return pairs      

        # i realized i over thought this but it works
nums = [1,2,2,1]
k = 1 
solution = Solution()
print(solution.countKDifference(nums, k))