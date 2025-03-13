class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {i:[] for i in s1}

        for i in range(len(s2)):
            if hashmap.get(s2[i], None) != None:
                hashmap[s2[i]].append(i)
                
        keys = list(hashmap.keys())
        
        for i in range(len(keys)-1):
            idx = hashmap[keys[i]]
            if len(idx) == 0:
                return False
            
            close = False
            for j in idx:
                for k in hashmap[keys[i+1]]:
                    if abs(j-k) == 1:
                        close = True
                        break
                if close:
                    break
            if not close:
                return False
        return True
                

            
            

s1 = "adc"
s2 = "dcda"
solution = Solution()
print(solution.checkInclusion(s1, s2))