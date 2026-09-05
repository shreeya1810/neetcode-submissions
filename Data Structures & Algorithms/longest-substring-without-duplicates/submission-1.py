class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
     if s=="":
        return 0
     i = 0
     curr = set()
     curr.add(s[i])
     longest = 1
     for j in range(1, len(s)):
        while s[j] in curr:
            curr.remove(s[i])
            i+=1
        curr.add(s[j])
        longest = max(longest, j-i+1)
        
     return longest