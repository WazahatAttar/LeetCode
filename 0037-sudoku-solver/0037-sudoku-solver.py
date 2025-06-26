class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [[False]*9 for _ in range(9)]
        col = [[False]*9 for _ in range(9)]
        box = [[False]*9 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    idx = int(board[r][c]) - 1
                    box_no = (r // 3) * 3 + (c // 3)
                    row[r][idx] = col[c][idx] = box[box_no][idx] = True

        def backtrack(r, c):
            if r == 9:
                return True

            next_r, next_c = (r + 1, 0) if c == 8 else (r, c + 1)

            if board[r][c] != '.':
                return backtrack(next_r, next_c)

            box_no = (r // 3) * 3 + (c // 3)
            for num in range(1, 10):
                idx = num - 1
                if not row[r][idx] and not col[c][idx] and not box[box_no][idx]:
                    board[r][c] = str(num)
                    row[r][idx] = col[c][idx] = box[box_no][idx] = True

                    if backtrack(next_r, next_c):
                        return True

                    board[r][c] = '.'
                    row[r][idx] = col[c][idx] = box[box_no][idx] = False

            return False

        backtrack(0, 0)