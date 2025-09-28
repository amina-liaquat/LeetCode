class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        first = abs(z - x)
        second = abs( z - y)
        if first == second:
            return 0
        return 1 if first < second else 2   
