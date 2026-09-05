class Solution:
    def isValid(self, s: str) -> bool:
        bracks={'(':')', '[':']', '{':'}'}
        stack=[]
        for c in s:
            if c in bracks:
                stack.append(c)
            else:
                if stack and bracks[stack[-1]]!=c:
                    return False
                if not stack:
                    return False
                stack.pop()
        if stack:
            return False
        return True