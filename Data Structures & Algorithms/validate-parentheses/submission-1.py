class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        maps = {"}": "{", "]": "[", ")": "("}

        for b in s:
            if not seen or b in "({[":
                seen.append(b)
            elif maps[b] == seen[-1]:
                seen.pop()
            else:
                return False
        
        return len(seen) == 0

