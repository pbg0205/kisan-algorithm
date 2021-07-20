"""
Runtime: 84 ms, faster than 63.87% of Python3 online submissions for Combination Sum.
Memory Usage: 14.4 MB, less than 23.84% of Python3 online submissions for Combination Sum.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        results = []
        
        def dfs(elements, current_sum, index):
            # ending condition
            if current_sum > target :
                return
            elif current_sum == target :
                results.append(elements)
                
            for i in range(index, len(candidates)):
                dfs(elements+[candidates[i]], current_sum+candidates[i], i)
                
        
        dfs([], 0, 0)
        
        return results
            
            
            
