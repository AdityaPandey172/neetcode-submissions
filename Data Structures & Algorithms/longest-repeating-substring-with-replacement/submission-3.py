class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        max_length = 0
        char_freq = {}
        max_freq = 0

        while right < len(s):
            char_freq[s[right]] = char_freq.get(s[right], 0) + 1
            max_freq = max(max_freq, char_freq[s[right]])

            if (right - left + 1) - max_freq > k:
                char_freq[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
            right += 1
        
        return max_length