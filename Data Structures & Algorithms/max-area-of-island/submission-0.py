class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if not grid:
            return 0
        area = 0


        islands = 0
        
        def bfs(r, c):
            q = deque()
            grid[r][c] = 0
            q.append((r, c))
            count = 1 
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col 
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    count += 1 
                    grid[nr][nc] = 0
            return count 
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))
        return area