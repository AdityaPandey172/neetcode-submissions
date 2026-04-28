class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start, partition):
            if start == len(s):
                result.append(partition[:])
                return

            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if is_palindrome(sub):
                    partition.append(sub)
                    backtrack(end, partition)
                    partition.pop()

        result = []
        backtrack(0, [])
        return result
        