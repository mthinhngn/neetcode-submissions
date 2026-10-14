class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        time = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directs = [[1,0], [-1,0], [0,1], [0,-1]]

        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()

                for dr, dc in directs:
                    nr, nc = r + dr, c + dc

                    if (nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == 1):

                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            time += 1
        
        if fresh > 0:
            return -1
        return time