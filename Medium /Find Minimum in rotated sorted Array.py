class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        # binary search
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1 
            else:
                r = mid
        return nums[l] # or nums[r]
# T.C = O(logn)
# S.C = O(1)
        
