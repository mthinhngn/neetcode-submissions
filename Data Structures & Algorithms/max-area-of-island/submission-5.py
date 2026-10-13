class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxA = 0

        if not grid:
            return 0
        
        def dfs(r,c):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] != 1):
                return 0
                
            if grid[r][c] == 1:
                grid[r][c] = "#"
            res = 1
            res += dfs(r-1,c)
            res += dfs(r+1, c)
            res += dfs(r,c+1) 
            res += dfs(r, c-1)
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxA = max(maxA, dfs(r,c)) 
        return maxA