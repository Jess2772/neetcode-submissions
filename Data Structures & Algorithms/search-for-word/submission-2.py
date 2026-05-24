class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        N = len(word)

        def dfs(r, c, i, visited):
            if (r, c) in visited or r >= R or r < 0 or c >= C or c < 0 or i >= N:
                return False
            
            visited.add((r, c))
            res = False
            if word[i] == board[r][c]:
                if i == N - 1:
                    return True
                res = dfs(r - 1, c, i + 1, visited) or dfs(r + 1, c, i + 1, visited) or dfs(r, c - 1, i + 1, visited) or dfs(r, c + 1, i + 1, visited)
            visited.remove((r, c))
            return res

        for r in range (R):
            for c in range(C):
                if dfs(r, c, 0, set()):
                    return True
        return False