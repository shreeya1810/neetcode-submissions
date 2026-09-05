class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        hashmap, window = {}, {}
        for c in s1:
            hashmap[c] = 1 + hashmap.get(c, 0)
        
        have, need = 0, len(hashmap)
        l = 0
        for r in range(0, len(s2)):
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                if s2[l] in hashmap and window[s2[l]] < hashmap[s2[l]]:
                    have -= 1 
                l += 1

            c = s2[r]
            window[c] = 1 + window.get(c, 0)

            if c in hashmap and window[c] == hashmap[c]:
                have += 1
            
            if have == need:
                return True
        
        return False
