class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)      
        for i in range(1, max(piles) + 1):
            hours = 0
            for p in piles:
                hours += math.ceil(p / i)  
            
            if hours <= h:
                res = i
                break  

        return res
