class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s,e = 1, max(piles)

        while s <= e:
            hours = 0

            mid = (s + e) // 2
            for p in piles:
                hours += math.ceil(p/mid)

            if hours <= h:
                e = mid - 1
            else:
                s = mid + 1

        return s
        
