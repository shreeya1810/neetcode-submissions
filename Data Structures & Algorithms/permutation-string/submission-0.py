class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # Count character frequencies in s1
        count = {}
        for c in s1:
            count[c] = 1 + count.get(c, 0)

        # Sliding window approach
        have, need = 0, len(s1)
        l = 0
        for r in range(len(s2)):
            char = s2[r]
            if char in count:
                count[char] -= 1
                if count[char] == 0:
                    have += 1
            if have == need:
                return True
            if r - l + 1 == len(s1):
                char = s2[l]
                if char in count:
                    if count[char] == 0:
                        have -= 1
                    count[char] += 1
                l += 1
        return False