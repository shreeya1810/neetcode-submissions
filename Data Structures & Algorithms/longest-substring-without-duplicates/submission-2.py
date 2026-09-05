class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest, i = 0, 0
        curr = set()
        for j in range(0, len(s)):
            while s[j] in curr:
                curr.remove(s[i])
                i += 1
            curr.add(s[j])
            longest = max(j - i + 1, longest)
        return longest