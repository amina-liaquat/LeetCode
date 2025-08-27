class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1
        heapq.heapify(stones)
        while len(stones)>1:
            temp=[]
            temp.append(heapq.heappop(stones))
            temp.append(heapq.heappop(stones))
            if temp[1]>temp[0]:
                heapq.heappush(stones,temp[0]-temp[1])
        if len(stones)>0:
            return -stones[0]
        return 0
        
