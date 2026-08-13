class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        sq = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                # for each entry in board,
                # one less from 9 i.e. 8
                entry = int(board[r][c]) - 1
                if (1 << entry) & rows[r]:
                    return False
                if (1 << entry) & cols[c]:
                    return False
                if (1 << entry) & sq[(r//3) * 3 + (c//3)]:
                    return False
                
                rows[r] |= (1 << entry)
                cols[c] |= (1 << entry)
                sq[(r//3) * 3 + (c//3)] |= (1 << entry)

        return True