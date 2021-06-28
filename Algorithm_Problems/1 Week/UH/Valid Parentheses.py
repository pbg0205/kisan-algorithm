class Solution:
    def isValid(self, s: str) -> bool:
        open_parentheses = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        stack = []
        
        for parentheses in s :
            if parentheses in open_parentheses :
                if not stack or open_parentheses[parentheses] != stack.pop():
                    return False
            else :
                stack.append(parentheses)
                    
        return len(stack) == 0
