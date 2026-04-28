class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        cur_end = 0
        farthest_reachable = 0

        for i in range(len(nums) - 1):
            farthest_reachable = max(farthest_reachable, i + nums[i])
            if i == cur_end:
                jumps += 1
                cur_end = farthest_reachable
        
        return jumps
        