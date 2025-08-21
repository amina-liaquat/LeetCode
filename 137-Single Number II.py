class Solution:
  def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        for i in freq:
            if freq[i] == 1:
                return i
        
