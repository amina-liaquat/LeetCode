class Solution:
    def search(self, x: List[int], target: int) -> int:
        n = len(x)
        
        def findK():
            if n == 1:
                return 0
            if n==2:
                if x[0]<x[1]: return 1
                else: return 0
            l=0
            r=n
            while l < r:
                m = (r + l) // 2
                if m==n-1 or x[m]>x[m+1]: return m
                if x[m]>x[l]: l=m
                else: r=m
            return m
        
        k=findK()
        
        if target >= x[0]:
            i = bisect_left(x, target, hi=k)
            if i<n and x[i] == target:
                return i
            return -1
        else:
            i = bisect_left(x, target, lo=k+1)
            if i<n and x[i] == target:
                return i
            return -1
        
