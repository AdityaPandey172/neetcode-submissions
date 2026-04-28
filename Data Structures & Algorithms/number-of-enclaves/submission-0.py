class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def erase_from(sr: int, sc: int) -> None:
            stack = [(sr, sc)]
            grid[sr][sc] = 0
            while stack:
                r, c = stack.pop()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        stack.append((nr, nc))
        
        for r in range(m):
            if grid[r][0] == 1:
                erase_from(r, 0)
            if grid[r][n - 1] == 1:
                erase_from(r, n - 1)
        
        for c in range(n):
            if grid[0][c] == 1:
                erase_from(0, c)
            if grid[m - 1][c] == 1:
                erase_from(m - 1, c)
        
        return sum(grid[r][c] == 1 for r in range(m) for c in range(n))
        