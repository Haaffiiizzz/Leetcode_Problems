if s.isdigit():
            return True
        
        if not s[0].isdigit() and s[0] != "-" and s[0] != "+" and s[0] != ".":
            return False
        
        if "+" in s and "-" in s:
            return False
        
        if "e" in s or "E" in s:
            if "." in s[s.index(e):-1]:
                return False
            if s[s.index(e):-1]
        
        if not s.isdigit() and len(s) == 1:
            return False
        if len(set(s)) == 1 and not s.isdigit():
            return False
        
        return True