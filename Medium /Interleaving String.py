class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        l = len(s1)
        m = len(s2)
        n = len(s3)
        
        # base
        if l + m != n:
            return False

        def dfs(i, j, k):
            # base
            if i == l and j == m and k == n:
                return True

            # main
            # explore all the possible ways
            if i < l and s1[i] == s3[k]:
                if dfs(i+1, j, k+1):
                    return True
            
            if j < m and s2[j] == s3[k]:
                if dfs(i, j+1, k+1):
                    return True
            
            return False

        # iterate s1 and s2 (0, 0)
        return dfs(0, 0, 0)

# understand --> done

# observation/ naive approach
# winning idea: we do not need to create all the substr of s1 and s2, because doing so will increase our time comp...


# solution
# pseudo code
# iterate s1 and s2 and confirm if that subsr are equal to s3[k]
# if we found it in s1 then we will recursively call the fun with value i+1
# but if we found it in s2 instead then we will recursively call the fun with value j+1

# at the end of s3 we will return true else false


# implementation
