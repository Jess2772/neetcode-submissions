class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[m - 1][m - 1] is the number of paths from grid[0][0] to grid[m - 1][n - 1]
        dp = [[0] * n for _ in range (m)]

        # you can move down or to the right, thats it
        neighbours = [(-1, 0), (0, -1)]

        for r in range (m):
            for c in range (n):
                if r == 0 and c == 0:
                    dp[r][c] = 1
                else:
                    for dr, dc in neighbours:
                        prev_r = r + dr
                        prev_c = c + dc
                        if prev_r >= 0 and prev_c >= 0:
                            dp[r][c] += dp[prev_r][prev_c]

        return dp[m - 1][n - 1]