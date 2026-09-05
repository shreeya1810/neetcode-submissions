class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []

        def backtrack(r = 0, cols = set(), posDiag = set(), negDiag = set(), board = [["."] * n for i in range(n)] ):

            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1, cols, posDiag, negDiag, board)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0, set(), set(), set(), [["."] * n for i in range(n)])
        return res