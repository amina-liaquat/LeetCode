class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        # intializing the window
        l,r=0,k-1
        res=float('inf')
        n=len(nums)
        while r<n:
            res=min(res,nums[r]-nums[l])
            l+=1
            r+=1
        return res
