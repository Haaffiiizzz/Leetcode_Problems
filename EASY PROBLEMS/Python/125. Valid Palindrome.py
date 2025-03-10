class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while right >= left:

            if s[right].isalnum() and s[left].isalnum():
                if s[right].lower() != s[left].lower():
                    
                    return False
                left +=1 
                right -= 1
            
            else:
                if not s[right].isalnum():
                    right -= 1
                if not s[left].isalnum():
                    left += 1
        
        return True

s = "A man, a plan, a canal: Panama"
solution = Solution()
print(solution.isPalindrome(s))