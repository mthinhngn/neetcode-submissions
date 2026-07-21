class Solution:
    def isValid(self, s: str) -> bool:


# Before vid:
# Seperate open and close. the order has to match 1-6
# After vid:
# Using hashmap to store the open bracket
# After the close bracket, the box is empty. return TRUE
# O(n) 

# stack close to Open to find
# if it is Open, append to the stack
# if it is close, pop the stack 

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
