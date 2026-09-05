class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        map = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']
            }
        
        digits = str(digits)
        res = []

        if digits == "":
            return []

        def backtrack(i, curr = ''):
            if i == len(digits):
                res.append(curr)
                return
            for letter in map[digits[i]]:
                backtrack(i + 1, curr + letter)
        
        backtrack(0, '')
        return res