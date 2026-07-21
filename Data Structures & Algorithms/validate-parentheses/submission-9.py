class Solution:
    def isValid(self, s: str) -> bool:
        
# stack because we need to look for the top 
# and stack is O(1) adding to the top
# the close has to match with the top open
# if stack not exist when close OR not match, return F
# if it is open, add to the stack
# return T of no more stack, else False

        stack = []
        closetoOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s: 
            if c in closetoOpen:
                if stack and stack[-1] == closetoOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False