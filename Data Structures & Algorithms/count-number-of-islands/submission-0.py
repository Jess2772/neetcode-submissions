class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        R = len(grid)
        C = len(grid[0])
        res = 0

        def dfs(r, c):
            if r >= R or r < 0 or c >= C or c < 0 or grid[r][c] == "0" or (r, c) in visited:
                return
            
            visited.add((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range (R):
            for c in range (C):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        
        return res


        