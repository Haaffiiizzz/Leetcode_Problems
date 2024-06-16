if s.isdigit():
            return True
        
        if not s[0].isdigit() and s[0] != "-" and s[0] != "+":
            return False
        
        if "+" in s and "-" in s:
            return False
        
        
        
        return True