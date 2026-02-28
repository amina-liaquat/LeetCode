class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        result = [0] * n
        
        # store index with value
        arr = list(enumerate(nums))
        
        def merge_sort(arr):
            mid = len(arr) // 2
            if mid:
                left = merge_sort(arr[:mid])
                right = merge_sort(arr[mid:])
                
                merged = []
                i = j = 0
                
                while i < len(left) or j < len(right):
                    
                    if j == len(right) or (i < len(left) and left[i][1] > right[j][1]):
                        result[left[i][0]] += len(right) - j
                        merged.append(left[i])
                        i += 1
                    else:
                        merged.append(right[j])
                        j += 1
                        
                return merged
            return arr
        
        merge_sort(arr)
        return result
