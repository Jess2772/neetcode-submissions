from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        longest = 0
        l = 0
        for r in range (len(s)):
            seen[s[r]] += 1

            most_freq = max(seen.values())
            while (r - l + 1) - k > most_freq:
                seen[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest
        