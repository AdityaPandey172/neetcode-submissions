class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = 1

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], 1 + dfs(x, y)) 

            return dp[i][j]

        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        max_path = 0

        for i in range(m):
            for j in range(n):
                max_path = max(max_path, dfs(i, j))
        
        return max_path
                 