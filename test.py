class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        
        mirror = list(s[:])
        
        indexList = [0]
        
        if len(set(s)) == 1:
                return len(s)
        
        for i, char in enumerate(s):
            if char == "1":
                indexList.append(i)
        indexList.append(len(s))
        
                
        for idx in range(1, len(indexList)-1):
            start = indexList[idx-1]
            one_index = indexList[idx]
            end = indexList[idx+1]
            before = s[start:one_index]
            after = s[one_index+1:end]
            
            if before.count("0") > 0 and after.count("0") > 0:
                for j in range(len(before)):
                    mirror[start + j] = "1"
                for j in range(len(after)):
                    mirror[one_index + 1 + j] = "1"
        return mirror.count("1")
         

        
        
        # n = len(s)
        # prev = None
        # for i, char in enumerate(s):
        #     count = 0
        #     if char == "1":
        #         foundAnother = False
        #         firstZero = False
        #         secondZero = False
    
        #         if not prev:
        #             start = 0
        #         else:
        #             start = prev
        #         ourOne = True
        #         for j, charj in enumerate(s[start:]):
        #             if charj == "0":
        #                 if j < i:
        #                     firstZero = True
        #                 else:
        #                     secondZero = True
                                                     
        #                 count += 1
        #             else:
        #                 if ourOne:
        #                     ourOne = False
        #                     continue
        #                 else:
        #                     foundAnother = True
        #                     break
        #         if prev:
        #             beforeIt = True
        #         prev = i + 1
        #         if firstZero and secondZero:
        #             biggest = max(biggest, count)
        #         afterIt = True if foundAnother else False
        # if biggest < 2:
        #     return s.count("1")    
        # if beforeIt and afterIt:
        #     return biggest + 3
        # elif beforeIt or afterIt:
        #     return biggest + 2
        # else:
        #     return biggest + 1
                    
                    
                
                
            
            
            
        
s = "1000100"
solution = Solution()
print(solution.maxActiveSectionsAfterTrade(s))