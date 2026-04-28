class Solution:
    def rob(self, nums: List[int]) -> int:
        def houseRobber(nums: List[int]) -> int:
            n = len(nums)
            if n == 0:
                return 0
            if n == 1:
                return nums[0] 
        
            prev = 0
            curr = 0

            for num in nums:
                temp = curr
                curr = max(prev + num, curr)
                prev = temp
            
            return curr
        
        if len(nums) == 1:
            return nums[0]
        
        return max(houseRobber(nums[1:]), houseRobber(nums[:-1]))
        