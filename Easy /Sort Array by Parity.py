class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
         # even = []
        # odd = []
        # for x in nums:
        #     if x % 2 == 0:
        #         even.append(x)
        #     else:
        #         odd.append(x)
        # return even + odd
        left = 0
        for right in range(len(nums)):
            if nums[right] % 2==0:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1
        return nums
