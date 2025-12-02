class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        maximum = (float("-inf"), -1)  
        submax  = (float("-inf"), -1)

        start = 0
        end = 0
        ans = []

      
        while end < k:
            if nums[end] > maximum[0]:
                maximum = (nums[end], end)
            end += 1

        ans.append(maximum[0])


        while end < len(nums):

            if maximum[0] >= submax[0]:
                submax = maximum

            new_pair = (nums[end], end)

           
            if new_pair[0] >= maximum[0]:
                maximum = new_pair

            start += 1
            end += 1

          
            if maximum[1] < start:
                maximum = submax

            if maximum[1] < start:
                maximum = (float("-inf"), -1)
                for i in range(start, end):
                    if nums[i] > maximum[0]:
                        maximum = (nums[i], i)

           
                submax = maximum

            ans.append(maximum[0])

        return ans
