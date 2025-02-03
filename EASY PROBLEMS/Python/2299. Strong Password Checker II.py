class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        checks = set()
        special = "!@#$%^&*()-+"

        for i in range(len(password)):
            if i < len(password)-1 and password[i] == password[i+1]:
                return False
            if password[i].isdigit():
                checks.add("dig")
            else:
                if password[i].islower():
                    checks.add("low")
                elif password[i].isupper():
                    checks.add("up")
                elif password[i] in special:
                    checks.add("spec")

        return len(checks) == 4
        
password = "IloveLe3tcode!"
solution = Solution()
print(solution.strongPasswordCheckerII(password))