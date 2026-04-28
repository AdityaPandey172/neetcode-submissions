class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs_iter(sr: int, sc: int) -> None:
            if board[sr][sc] != "O":
                return

            stack = [(sr, sc)]
            board[sr][sc] = "E"

            while stack:
                r, c = stack.pop()

                if r + 1 < m and board[r + 1][c] == "O":
                    board[r + 1][c] = "E"
                    stack.append((r + 1, c))

                if r - 1 >= 0 and board[r - 1][c] == "O":
                    board[r - 1][c] = "E"
                    stack.append((r - 1, c))
                
                if c + 1 < n and board[r][c + 1] == "O":
                    board[r][c + 1] = "E"
                    stack.append((r, c + 1))
                
                if c - 1 >= 0 and board[r][c - 1] == "O":
                    board[r][c - 1]  = "E"
                    stack.append((r, c - 1))
                
    
        for row in range(m):
            dfs_iter(row, 0)
            dfs_iter(row, n - 1)

        for col in range(n):
            dfs_iter(0, col)
            dfs_iter(m - 1, col)

        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "E":
                    board[row][col] = "O"






