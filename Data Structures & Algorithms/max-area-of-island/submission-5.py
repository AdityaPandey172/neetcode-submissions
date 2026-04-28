class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        max_area = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs_iter(sr: int, sc: int) -> int:
            stack = [(sr, sc)]
            grid[sr][sc] = 0
            area = 0
        
            while stack:
                r, c = stack.pop()
                area += 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        stack.append((nr, nc))
            return area
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs_iter(r, c))
        
        return max_area



