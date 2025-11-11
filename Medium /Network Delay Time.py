class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times: #adj list
            edges[u].append((v, w)) #all neighbors of every node
        
        minHeap = [(0, k)] #from start to start, set by default
        visited = set()
        time = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap) #pop the smallest-weighted node
            if n1 in visited:
               continue
            visited.add(n1)
            time = max(time, w1) #update time to get to node

            for n2, w2 in edges[n1]: #BFS to explore node's neighbors 
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1+w2, n2))
        
        return time if len(visited) == n else -1 # set==n means all nodes viisited
