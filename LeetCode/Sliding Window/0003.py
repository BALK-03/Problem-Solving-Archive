class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                window = r - l + 1
                longest = max(longest, window)
                continue
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
        return longest