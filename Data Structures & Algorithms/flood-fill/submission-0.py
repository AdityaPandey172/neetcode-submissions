class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or not image[0]:
            return image
        
        m, n = len(image), len(image[0])
        old = image[sr][sc]
        if old == color:
            return image
    
        q = deque([(sr, sc)])
        image[sr][sc] = color
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc =  r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == old:
                    image[nr][nc] = color
                    q.append((nr, nc))
        
        return image