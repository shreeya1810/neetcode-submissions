class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        columns = len(grid[0])

        visited = set()
        area = 0
        def dfs(r, c):
            if r==rows or c==columns or r<0 or c<0 or grid[r][c]==0 or (r, c) in visited:
                return 0
            else:
                visited.add((r,c))
                return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)

        for i in range(rows):
            for j in range(columns):
                if grid[i][j]==1:
                    area = max(area, dfs(i, j))
        return area
        
