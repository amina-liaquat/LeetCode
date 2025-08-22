class Solution:
    def maxArea(self, height: List[int]) -> int:
        # res = 0
        # for l in range(len(height)):
        #     for r in range(l+1,len(height)):
        #         area = (r - l) * min(height[l],height[r])
        #         res = max(res,area)
        # return res

        res = 0
        left , right  = 0 , len(height) - 1
        while left < right:
            area = (right - left) * min(height[left],height[right])
            res = max(res,area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
        
