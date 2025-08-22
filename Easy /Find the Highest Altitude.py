class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = 0
        curAltitude = 0
        for g in gain:
             curAltitude += g
             maxAltitude = max(maxAltitude,curAltitude)

        return maxAltitude 
