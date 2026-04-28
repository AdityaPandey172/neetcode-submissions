class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}

        for i, char in enumerate(s):
            last_index[char] = i
        
        result = []
        start, end = 0, 0

        for i, char in enumerate(s):
            end = max(end, last_index[char])

            if i == end:
                result.append(end - start + 1)
                start = end + 1
        
        return result