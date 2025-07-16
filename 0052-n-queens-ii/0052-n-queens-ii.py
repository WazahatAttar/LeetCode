class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.'] * n for _ in range(n)]
        count = [0]
        def is_safe(row, col):
            for c in range(col):
                if board[row][c] == 'Q':
                    return False
            r, c = row, col
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1
            r, c = row, col
            while r < n and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r += 1
                c -= 1
            return True
        def backtrack(col):
            if col == n:
                count[0] += 1  
                return
            for row in range(n):
                if is_safe(row, col):
                    board[row][col] = 'Q'   
                    backtrack(col + 1)
                    board[row][col] = '.'  
        backtrack(0)
        return count[0]