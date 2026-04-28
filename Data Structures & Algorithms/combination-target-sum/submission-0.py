class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, combination):
            if target == 0:
                result.append(
                    combination[:]
                )
                return
            
            for i in range(start, len(nums)):
                if nums[i] > target:
                    continue

                combination.append(nums[i])
                backtrack(i, target - nums[i], combination)
                combination.pop()

        result = []
        backtrack(0, target, [])
        return result

