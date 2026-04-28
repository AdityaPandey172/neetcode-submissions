class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_length = 0
        unique_chars = set()

        while right < len(s):
            if s[right] not in unique_chars:
                unique_chars.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                unique_chars.remove(s[left])
                left += 1
        
        return max_length