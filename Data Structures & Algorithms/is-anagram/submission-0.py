class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = [0] * 26

        for c in s:
            seen[ord(c) - ord('a')] += 1
        
        for c in t:
            seen[ord(c) - ord('a')] -= 1
            
        if seen == [0] * 26:
            return True
        return False