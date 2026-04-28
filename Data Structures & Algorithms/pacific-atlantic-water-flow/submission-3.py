class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs_iter(sr, sc, reachable):
            stack = [(sr, sc)]
            reachable.add((sr, sc))
            while stack:
                r, c = stack.pop()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols
                        and (nr, nc) not in reachable
                        and heights[nr][nc] >= heights[r][c]):
                        reachable.add((nr, nc))
                        stack.append((nr, nc))

        for r in range(rows):
            if (r, 0) not in pac:
                dfs_iter(r, 0, pac)
            if (r, cols - 1) not in atl:
                dfs_iter(r, cols - 1, atl)

        for c in range(cols):
            if (0, c) not in pac:
                dfs_iter(0, c, pac)
            if (rows - 1, c) not in atl:
                dfs_iter(rows - 1, c, atl)

        return [[r, c] for (r, c) in (pac & atl)]
