class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        pq = [(0, 0, 0)] #(effort, r, c)
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            diff, r, c = heapq.heappop(pq)
            if (r, c) in visited:
                continue
            visited.add((r, c))

            if (r, c) == (rows - 1, cols - 1):
                return diff 

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    nd = max(diff, abs(heights[r][c] - heights[nr][nc]))
                    heapq.heappush(pq, (nd, nr, nc))

        return 0       