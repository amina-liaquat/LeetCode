class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        newNum = set(nums)
        for i in newNum: 
            if nums.count(i) == 1:
                return i
