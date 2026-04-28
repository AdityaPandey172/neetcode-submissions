class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        char_freq_s1 = {}
        for char in s1:
            char_freq_s1[char] = char_freq_s1.get(char, 0) + 1
        
        left, right = 0, 0
        char_freq_temp = {}

        while right < len(s2):
            char_freq_temp[s2[right]] = char_freq_temp.get(s2[right], 0) + 1

            if right - left + 1 == len(s1):
                if char_freq_temp == char_freq_s1:
                    return True
                char_freq_temp[s2[left]] -= 1
                if char_freq_temp[s2[left]] == 0:
                    del char_freq_temp[s2[left]]
                left += 1

            right += 1
        
        return False



        