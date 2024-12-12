class Solution:
    def pickGifts(gifts: list[int], k: int) -> int:
        import math
        while k > 0:
            high = max(gifts)
            leave = math.isqrt(high)
            gifts[gifts.index(high)] = leave
            k -= 1
        return sum(gifts)
gifts = [25,64,9,4,100]
k = 4
print(Solution.pickGifts(gifts, k))         
