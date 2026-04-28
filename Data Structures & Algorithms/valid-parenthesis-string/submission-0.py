class Solution:
    def checkValidString(self, s: str) -> bool:
        lower = upper = 0

        for char in s:
            if char == "(":
                lower += 1
                upper += 1
            elif char == ")":
                lower = max(lower - 1, 0)
                upper -= 1
            else:
                lower = max(lower - 1, 0)
                upper += 1
            
            if upper < 0:
                return False
        
        return lower == 0
        