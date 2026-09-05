
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(i, j, curr='', visited = set()):
            if curr == word:
                return True
            
            if len(curr) == len(word):
                return False
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            
            if (i, j) in visited or board[i][j] != word[len(curr)]:
                return False
            
            visited.add((i, j))
            
            # don't return false if not there, explore next tree
            if (backtrack(i+1, j, curr + board[i][j], visited) or
                backtrack(i, j+1, curr + board[i][j], visited) or
                backtrack(i-1, j, curr + board[i][j], visited) or
                backtrack(i, j-1, curr + board[i][j], visited)):
                return True
            
            visited.remove((i, j))
            
            return False
        
        # Check each cell in the board as a starting point
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j):
                    return True
        
        return False