class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(row, col):
            for prev_row in range(row):
                if board[prev_row][col] == "Q":
                    return False
                if(
                    col - (row - prev_row) >= 0
                    and board[prev_row][col - (row - prev_row)] == "Q"
                ):
                    return False
                if(
                    col + (row - prev_row) < n
                    and board[prev_row][col + (row - prev_row)] == "Q"
                ):
                    return False
            return True
        
        def place_queen(row):
            if row == n:
                result.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = "Q"
                    place_queen(row + 1)
                    board[row][col] = "."
        
        board = [["." for _ in range(n)] for _ in range(n)]
        result = []
        place_queen(0)
        return result


        