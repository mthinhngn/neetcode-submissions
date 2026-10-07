class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        count = 0

        def dfs(r,c):
            if (r in range(rows) and c in range(cols) and
                grid[r][c] == "1" and (r,c) not in visit):
                visit.add((r,c))
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r, c+1)
                dfs(r,c-1)
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    count += 1
        
        return count