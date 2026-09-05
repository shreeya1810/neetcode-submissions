class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res=[]
        def backtrack(sum, current, i):
            if sum>target or i>=len(nums):
                return
            if sum==target:
                res.append(current.copy())
                return

            current.append(nums[i])
            backtrack(sum+nums[i], current, i)
            current.pop()
            backtrack(sum, current, i+1)
            return res

        return backtrack(sum=0, current=[], i=0)