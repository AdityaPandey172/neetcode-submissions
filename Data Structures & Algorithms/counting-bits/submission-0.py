class Solution:
    def countBits(self, n: int) -> List[int]:
        bits_count = [0] * (n + 1)

        for i in range(1, n + 1):
            bits_count[i] = bits_count[i // 2] + (i % 2)
        
        return bits_count
        