class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        i = 0
        n = len(arr)
        while i < n-2:
            if arr[i] % 2 != 0:
                if arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                    return True
                i += 2
            else:
                i += 1
        return False 
arr = [2,6,4,1]
solution = Solution()
print(solution.threeConsecutiveOdds(arr))