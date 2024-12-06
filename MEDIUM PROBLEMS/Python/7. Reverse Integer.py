class Solution:
    def reverse(self, x: int) -> int:
        
        strVer = str(x)
        prefix = False
        if strVer[0] == "-":
            prefix = True
            strVer = strVer[1:]
        
        if prefix:
            strVer += "-"
        newStr = strVer[::-1]
        num = int(newStr)
        
        if  num < -2**31 or num > (2**31) - 1:
            return 0
        return num