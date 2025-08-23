class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        lf = 0
        maxlen = 0
        for rt in range(1,len(nums)): # range can be from first index to last index or zero to last index
            while nums[rt] - nums[lf] > 1:
                lf += 1
            if nums[rt] - nums[lf] == 1:
                maxlen = max(maxlen, rt -lf + 1)    
        return maxlen
