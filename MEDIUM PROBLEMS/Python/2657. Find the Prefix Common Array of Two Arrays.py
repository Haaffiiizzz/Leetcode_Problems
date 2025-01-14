class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        # C = [0]*len(A)

        # for i in range(len(C)):
        #     Apart = A[0:i+1]
        #     Bpart = B[0:i+1]

        #     C[i] = len(Apart+Bpart) - len(set(Apart+Bpart))
        
        # return C
        
        C = []
        ASeen = set()
        BSeen = set()
        dup = 0
        for i in range(len(A)):
            if A[i] in BSeen:
                dup += 1
            ASeen.add(A[i])

            if B[i] in ASeen:
                dup += 1
            BSeen.add(B[i])


            C.append(dup)
        
        return C
    
#better solution
    
A = [1,3,2,4]
B = [3,1,2,4]
solution = Solution()
print(solution.findThePrefixCommonArray(A, B))