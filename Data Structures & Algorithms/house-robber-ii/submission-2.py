class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(l: int, r: int) -> int:
            prev2 = 0
            prev1 = 0
            for i in range(l, r + 1):
                prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
            return prev1
        
        return max(rob_linear(0, n - 2), rob_linear(1, n - 1))