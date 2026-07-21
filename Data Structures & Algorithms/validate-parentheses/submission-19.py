class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_bracket = ['(', '[', '{']
        close_bracket = [')', ']', '}']
        match = {')' : '(', '}' : '{', ']' : '['}

        for ch in s:
            if ch in open_bracket:
                stack.append(ch)
            elif ch in close_bracket:
                if not stack or match[ch] != stack[-1]:
                    return False
                stack.pop()
            pass
        return not stack    
            
    '''
    use a stack
    create a dict that set the pair of open bracket and close bracket
    loop it, every open bracket append to the stack, 
    if the close bracket match with an open bracket, pop it 
    '''
