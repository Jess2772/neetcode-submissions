from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        l, r = 0, 0
        seen = defaultdict(int)

        while r < n:
            seen[s[r]] += 1

            while max(seen.values()) > 1:
                seen[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
            r += 1

        return longest
        
            


        

            

        