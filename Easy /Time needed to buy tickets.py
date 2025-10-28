class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q=deque([(i,t) for i,t in enumerate(tickets)])
        time=0
        while q:
            i,t=q.popleft()
            t-=1
            time+=1
            if t>0:
                q.append((i,t))
            if i==k and t==0:
                return time


       
        # T: O(n*m)
        # S: O(n)
