class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset= set(nums)
        if len(myset) == len(nums):
            return False 
        else:
            return True
