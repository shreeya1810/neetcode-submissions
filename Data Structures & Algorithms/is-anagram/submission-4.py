class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted, t_sorted = sorted(s), sorted(t)
        if s_sorted == t_sorted:
            return True
        else:
            return False