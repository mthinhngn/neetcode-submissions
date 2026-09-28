class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping_stack = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in mapping_stack:
                if stack and stack[-1] == mapping_stack[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False