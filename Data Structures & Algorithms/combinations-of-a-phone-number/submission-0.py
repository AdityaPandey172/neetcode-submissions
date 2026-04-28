class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, combination):
            if index == len(digits):
                combinations.append(combination)
                return
            
            digit = digits[index]
            letters = phone_mapping[digit]

            for letter in letters:
                backtrack(index + 1, combination + letter)
        
        combinations = []
        backtrack(0, "")
        return combinations

        