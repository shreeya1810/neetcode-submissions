
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(i, j, curr='', visited = set()):
            # If the current word is the target word
            if curr == word:
                return True
            
            # If the current word length exceeds the target word's length
            if len(curr) == len(word):
                return False
            
            # Boundary conditions
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            
            # If the cell is already visited or doesn't match the next character in the word
            if (i, j) in visited or board[i][j] != word[len(curr)]:
                return False
            
            # Add the cell to the path
            visited.add((i, j))
            
            # Explore in all 4 directions
            if (backtrack(i+1, j, curr + board[i][j], visited) or
                backtrack(i, j+1, curr + board[i][j], visited) or
                backtrack(i-1, j, curr + board[i][j], visited) or
                backtrack(i, j-1, curr + board[i][j], visited)):
                return True
            
            # Backtrack: remove the cell from the path
            visited.remove((i, j))
            
            return False
        
        # Check each cell in the board as a starting point
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j):
                    return True
        
        return False