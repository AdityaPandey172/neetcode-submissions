class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        char_freq_t = {}
        for char in t:
            char_freq_t[char] = char_freq_t.get(char, 0) + 1

        left, right = 0, 0
        char_freq_temp = {}
        required_chars = len(char_freq_t)
        formed_chars = 0
        min_length = float("inf")
        min_window = ""

        while right < len(s):
            char_freq_temp[s[right]] = char_freq_temp.get(s[right], 0) + 1

            if(
                s[right] in char_freq_t
                and char_freq_temp[s[right]] == char_freq_t[s[right]]
            ):
                formed_chars += 1
            
            while left <= right and formed_chars == required_chars:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left : right + 1]
                
                char_freq_temp[s[left]] -= 1
                if(
                    s[left] in char_freq_t
                    and char_freq_temp[s[left]] < char_freq_t[s[left]]
                ):
                    formed_chars -= 1
                
                left += 1

            right += 1

        return min_window  