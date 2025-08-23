class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res , maxCount = 0 , 0
        for n in nums:
            count[n] = 1 + count.get(n,0) 
            if count[n] > maxCount:
                res = n
            maxCount = max(count[n],maxCount)
        return res

        
