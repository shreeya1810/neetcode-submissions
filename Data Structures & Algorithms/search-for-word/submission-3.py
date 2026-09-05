class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def backtrack(i, r, c, visited):
            # Check if we've matched the entire word
            if i == len(word):
                return True
            # Check for out-of-bounds, character mismatch, or revisited cell
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i] or (r, c) in visited:
                return False

            # Add the current cell to visited
            visited.add((r, c))
            
            # Explore all four directions: down, up, right, left
            res = (backtrack(i + 1, r + 1, c, visited) or
                   backtrack(i + 1, r - 1, c, visited) or
                   backtrack(i + 1, r, c + 1, visited) or
                   backtrack(i + 1, r, c - 1, visited))

            # Backtrack by removing the current cell from visited
            visited.remove((r, c))
            
            return res

        # Iterate over every cell in the board as a starting point
        for i in range(rows):
            for j in range(cols):
                if backtrack(0, i, j, set()):  # Start backtracking from each cell
                    return True
        
        return False
