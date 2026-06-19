class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # ignore ".", its like they dont even exist

        # validate rows
        # validate columns
        # validate the squares

        for row in board:
            seen = set()
            for element in row:
                if element != ".":
                    if element in seen:
                        print('a')
                        return False
                    seen.add(element)

        for i in range (9):
            seen = set()
            for j in range (9):
                element = board[j][i]
                if element != ".":
                    if element in seen:
                        print('b')
                        return False
                    seen.add(element)

        for i in range (9):
            seen = set()
            start_r = (i // 3) * 3
            start_c = (i % 3) * 3
            for j in range (9):
                r = start_r + (j // 3)
                c = start_c + (j % 3)

                element = board[r][c]
                if element != ".":
                    if element in seen:
                        return False
                    seen.add(element)
        return True

    
                
                


        