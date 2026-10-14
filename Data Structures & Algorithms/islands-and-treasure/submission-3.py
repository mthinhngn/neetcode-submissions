class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        rows, cols = len(grid), len(grid[0])
        q = deque()

        # Add every treasure to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Out of bounds
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue

                # Only visit INF cells
                if grid[nr][nc] != 2147483647:
                    continue

                # Neighbor distance = current distance + 1
                grid[nr][nc] = grid[r][c] + 1

                q.append((nr, nc))