class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        res = nums[0] + nums[1] + nums[2]
                
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    l += 1
                else:
                    r -= 1
                            
        return res
        
