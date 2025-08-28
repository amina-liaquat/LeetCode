class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and arr[mid] < arr[mid-1]:
                right = mid - 1
            elif mid < len(arr)-1 and arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                return mid
        
