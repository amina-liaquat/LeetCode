class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: 
            return [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: 
                b, e = mid, mid
                while e < len(nums) and nums[e] == target: 
                    e += 1 #to go at ending target value
                while b >= 0 and nums[b] == target: 
                    b -= 1 #to go at starting target value
                if b != mid: 
                    b += 1 #previous position catch kr len
                if e != mid: 
                    e -= 1 #previous position catch kr len

                return [b, e]

            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [-1, -1]
