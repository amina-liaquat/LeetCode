class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0] #first value
        for n in nums:
            if abs(n) < abs(closest):
                closest = n
        
        # if we have both values e.g -1 and 1
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
