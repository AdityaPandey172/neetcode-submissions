class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols =  len(grid), len(grid[0])
        fresh_count = 0
        rotten = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        minutes = 0

        while rotten and fresh_count > 0:
            level_size = len(rotten)
            minutes += 1

            for _ in range(level_size):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc 
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        rotten.append((nr, nc))
        
        

        return minutes if fresh_count == 0 else -1
