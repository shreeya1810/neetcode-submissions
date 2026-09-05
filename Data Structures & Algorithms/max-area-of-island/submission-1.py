class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        area = 0
        rows, columns = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r==rows or c==columns or grid[r][c]==0 or (r, c) in visited:
                return 0
            visited.add((r,c))
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        for r in range(rows):
            for c in range(columns):
                if grid[r][c]==1:
                    area = max(area, dfs(r, c))
        return area