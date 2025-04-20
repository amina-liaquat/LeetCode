from typing import List
from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = {}

        for i in range(n):
            adj_list[i] = []

        m = len(flights)
        for i in range(m):
            u = flights[i][0]
            v = flights[i][1]
            wt = flights[i][2]

            adj_list[u].append((v, wt))
        
        cost = [float("inf")] * n
        q = deque()

        cost[src] = 0
        q.append((0, 0, src))

        while q:
            stop, cos, node = q.popleft()

            if stop > k:
                continue
            
            for i in range(len(adj_list[node])):
                adj_node = adj_list[node][i][0]
                adj_wt = adj_list[node][i][1]

                if cos + adj_wt < cost[adj_node]:
                    cost[adj_node] =  cos + adj_wt
                    q.append((stop+1, cos + adj_wt, adj_node))
                
        if cost[dst] == float("inf"):
            return -1
        
        return cost[dst]
