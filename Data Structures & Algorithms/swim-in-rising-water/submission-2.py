class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [(grid[0][0], 0, 0)]
        visited = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == n - 1 and c == n - 1:
                return t

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    heapq.heappush(minHeap, (max(t, grid[nr][nc]), nr, nc))    