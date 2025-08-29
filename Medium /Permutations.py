class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        two arrays --> recursion --> base case --> loop --> backtrack -->pop element --> result
        """
        n=len(nums)
        res =[] #final
        sol=[] # update
        def back_track():
            if len(sol)==n:
                res.append(sol[:]) # copying 0 index to last index
                return
            for i in nums:
                if i not in sol: # duplicate 
                    sol.append(i) # CHOICE ADD
                    back_track() # recurs
                    sol.pop() # remove
        back_track()
        return res
        
