from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        boxes = defaultdict(list)
        for r in range (9):
            for c in range(9):
                cell = board[r][c]
                if cell != ".":
                    if cell in rows[r] or cell in cols[c] or cell in boxes[(r // 3, c // 3)]:
                        return False
                    
                    rows[r].append(cell)
                    cols[c].append(cell)
                    boxes[(r // 3, c // 3)].append(cell)

        return True

                