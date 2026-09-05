class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPali(sub):
            return sub == sub[::-1]

        res = []

        def backtrack(start, curr = []):
            if start == len(s):
                res.append(curr[:])
            for i in range(start, len(s)):
                if isPali(s[start:i+1]):
                    curr.append(s[start:i+1])
                    backtrack(i + 1, curr)
                    curr.pop()
        
        backtrack(0, [])
        return res
            
            
            