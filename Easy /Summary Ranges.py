class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        start = nums[0]
        end = nums[0]
        res =[]
        for i in range(1,len(nums)):
            print(i)
            if nums[i] != nums[i-1] +1:
                if start == end:
                    res.append(f'{start}')
                else:
                    res.append(f'{start}->{end}')
                start=nums[i]
                end=nums[i]
            else:
                end = nums[i]
                
        if start!=end and f'{start}->{end}' not in res:
            res.append(f'{start}->{end}')
        elif f'{start}' not in res:
            res.append(f'{start}')
        return res
        
