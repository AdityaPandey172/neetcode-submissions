class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(row, col):
            if(
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or grid[row][col] == "0"
            ):
                return
            
            grid[row][col] = "0"
            directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                dfs(row + dr, col + dc)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        
        return count