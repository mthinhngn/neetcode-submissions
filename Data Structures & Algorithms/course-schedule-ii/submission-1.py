class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preM = {i: [] for i in range(numCourses)}
        visit = set()
        complete = set()
        res = []

        for crs, pre in prerequisites:
            preM[crs].append(pre)

        def dfs(crs):
            if crs in visit:
                return False
            
            if crs in complete:
                return True
            
            visit.add(crs)
            
            for pre in preM[crs]:
                if not dfs(pre):
                    return False
            
            visit.remove(crs)
            complete.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res 