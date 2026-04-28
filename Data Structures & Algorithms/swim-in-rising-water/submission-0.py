class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def dfs(i, j, visited, time):
            if i < 0 or i >= N or j < 0 or j >= N or visited[i][j] or grid[i][j] > time:
                return False
            if i == N - 1 and j == N - 1:
                return True
            visited[i][j] = True
            return(
                dfs(i + 1, j, visited, time)
                or dfs(i - 1, j, visited, time)
                or dfs(i, j + 1, visited, time)
                or dfs(i, j - 1, visited, time)
            )

        N = len(grid)
        left, right = 0, N * N

        while left < right:
            mid = (left + right) // 2
            visited = [[False] * N for _ in range(N)]
            if dfs(0, 0, visited, mid):
                right = mid 
            else:
                left = mid + 1
        
        return left