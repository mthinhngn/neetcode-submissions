class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxA= 0

        if not grid:
            return 0

        def dfs(r, c):
            if (r not in range(rows) or 
                c not in range(cols) or 
                grid[r][c] == 0 or
                (r,c) in visit):
                return 0
            
            visit.add((r,c))

            res = 1
            res += dfs(r+1,c)
            res += dfs(r-1,c)
            res += dfs(r,c+1)
            res += dfs(r,c-1)

            return res
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    maxA = max(maxA, dfs(r,c))
        return maxA