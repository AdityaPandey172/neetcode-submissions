class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        
        target = s // 2
        if max(nums) > target:
            return False

        dp = {0}
        for x in nums:
            nextDP = set(dp)
            for t in dp:
                if t + x <= target:
                    nextDP.add(t + x)
            dp = nextDP
            if target in dp:
                return True
        return False        