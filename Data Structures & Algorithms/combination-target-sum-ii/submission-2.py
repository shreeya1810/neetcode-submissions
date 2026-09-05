class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()  # Sort candidates to handle duplicates
        res = []

        def backtrack(i = 0, curr = [], currSum = 0):
            if currSum == target:
                res.append(curr.copy())  # Use copy to avoid issues with list mutability
                return
            if currSum > target or i == len(candidates):
                return

            # Include candidates[i]
            backtrack(i + 1, curr + [candidates[i]], currSum + candidates[i])

            # Skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # Exclude candidates[i]
            backtrack(i + 1, curr, currSum)

        backtrack(0, [], 0)
        return res
