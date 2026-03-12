class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        D = defaultdict(list)
        for u, v in edges:
            D[u].append(v)
            D[v].append(u)
        def dfs(node):
            if node == destination:
                return True
            for nei_node in D[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    if dfs(nei_node):
                        return True
            return False
        seen = set()
        seen.add(source)
        return dfs(source)
