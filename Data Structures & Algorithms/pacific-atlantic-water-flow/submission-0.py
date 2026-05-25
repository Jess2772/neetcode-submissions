class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        ROWS, COLS = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            if (r, c) in visited:
                return False
            
            visited.add((r, c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS) and heights[r][c] <= heights[nr][nc]:
                    dfs(nr, nc, visited)
                    

        for c in range (COLS):
            dfs(0, c, atlantic)
            dfs(ROWS - 1, c, pacific)

    
        for r in range (ROWS):
            dfs(r, 0, atlantic)
            dfs(r, COLS - 1, pacific)

        return list(pacific & atlantic)