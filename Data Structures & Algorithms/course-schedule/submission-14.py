class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preM = {i : [] for i in range(numCourses)}
        visit = set()

        for crs, pre in prerequisites:
            preM[crs].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return False
            if preM[crs] == []:
                return True
            
            visit.add(crs)
            for pre in preM[crs]:
                if not dfs(pre):
                    return False
            
            visit.remove(crs)
            preM[crs] = []
            return True
            
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True