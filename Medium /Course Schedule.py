class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            #cycle detected
            if crs in visited:
                return False
            #no-more prerequisites (end node)
            if preMap[crs] == []:
                return True
            
            visited.add(crs)
            #go-to the prerequisites
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            #empty the prerequisites after going through a node
            preMap[crs]=[]
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
        
