# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        result = 0
        while low <= high:
            mid = (low + high)//2
            if isBadVersion(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return result
