class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, combination):
            if target == 0:
                result.append(
                    combination[:]
                )
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i -1]:
                    continue
                
                if candidates[i] > target:
                    continue
                
                combination.append(candidates[i])
                backtrack(i + 1, target - candidates[i], combination)
                combination.pop()
        
        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result