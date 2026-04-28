class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0

        for i, jump_length in enumerate(nums):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + jump_length)
        
        return True