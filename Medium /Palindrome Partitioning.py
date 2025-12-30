class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        DP + Recursion
        """
        res=[]
        part=[]
        def isPali(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return  False
                l+=1
                r-=1
            return True

        def dfs(i):
            if i>=len(s):
                res.append(part.copy())
                return
                # recursive case
            for j in range(i,len(s)):
                substring=s[i:j+1]
                if substring ==substring[::-1]:
                    part.append(substring)
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
