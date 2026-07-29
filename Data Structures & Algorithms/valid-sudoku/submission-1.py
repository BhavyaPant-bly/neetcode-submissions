class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box = [set() for _ in range(9)]
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]

        for i in range (0,9):
            for j in range(0,9):
                x=board[i][j]
                if '1' <= x <= '9':
                    index=3*(i//3)+(j//3)
                    if x in box[index] or x in row[i] or x in col[j]:
                        return False
                    box[index].add(x)
                    row[i].add(x)
                    col[j].add(x)
        return True
        