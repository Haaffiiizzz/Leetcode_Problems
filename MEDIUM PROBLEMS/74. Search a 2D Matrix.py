class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def search(nums: List[int], target: int) -> int:
            
            #normal binary search but with a twist to make the second part easier
            if nums[0] > target:
                return -1
            if nums[-1] < target:
                return 1
            
            low = 0
            high = len(nums) -1

            while low <= high:
                middle = (low + high) // 2

                if nums[middle] == target:
                    return 0
                else:
                    if nums[middle] < target:
                        low = middle + 1
                    else:
                        high = middle - 1
            return -2
        
        high = len(matrix) - 1
        low = 0
        
        while low <= high:
            middle = (low + high) // 2
            array = matrix[middle]
            searchRes = search(array, target)
            if searchRes == 0:
                return True
            elif searchRes == -1:
                high = middle -1
            else:
                low = middle + 1
        return False
            
            
            
                