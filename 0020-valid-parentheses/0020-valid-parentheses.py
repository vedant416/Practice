class Solution:
    def isValid(self, s: str) -> bool:
        hm = {
            "}" : "{" ,
            "]" : "[" ,
            ")" : "("
        }
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    return False
                elif stack[-1] == hm[c]:
                    stack.pop()
                else:
                    return False
                
        if len(stack) > 0:
            return False
        else:
            return True
        