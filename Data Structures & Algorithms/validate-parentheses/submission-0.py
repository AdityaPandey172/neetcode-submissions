class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {")" : "(", "}" : "{", "]" : "["}
        
        for char in s:
            if char in parentheses_map.values():
                stack.append(char)
            elif char in parentheses_map:
                if not stack or stack[-1] != parentheses_map[char]:
                    return False
                stack.pop()
            else:
                return False

        return not stack                    
