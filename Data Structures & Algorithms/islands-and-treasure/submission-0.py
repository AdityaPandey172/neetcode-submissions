class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        rows, cols = len(grid), len(grid[0])
        gates = [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == 0]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for gate_row, gate_col in gates:
            visited = set()  # To track visited cells in BFS
            queue = deque([(gate_row, gate_col, 0)])

            while queue:
                row, col, distance = queue.popleft()
                grid[row][col] = min(grid[row][col], distance)
                visited.add((row, col))

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    
                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and grid[new_row][new_col] != -1
                        and (new_row, new_col) not in visited
                    ):
                        queue.append((new_row, new_col, distance + 1))
                        visited.add((new_row, new_col))
