class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l , r = 0, n-1
        if len(nums) == 1:
            return nums[0]

        while l<=r:
            mid = r + (l-r) // 2
            if mid == 0 and nums[0] != nums[1]:
                return nums[mid]
            if mid == n-1 and nums[n-1]!=nums[n-2]:
                return nums[mid]
                
            if nums[mid-1] != nums[mid] and nums[mid]!=nums[mid + 1]:
                return nums[mid]

            if mid % 2 ==0: #even numbers on bs
                if nums[mid-1] == nums[mid]:
                    r = mid -1
                else: 
                    l = mid + 1

            else:
                if nums[mid-1]==nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
