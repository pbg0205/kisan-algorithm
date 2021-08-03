"""
Runtime: 448 ms, faster than 71.59% of Python3 online submissions for Combinations.
Memory Usage: 15.8 MB, less than 22.14% of Python3 online submissions for Combinations.
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # dfs
        results = []
        
        def dfs(elements, start, k):
            # ending condition
            if k == 0:
                results.append(elements.copy())
                return
            
            for e in range(start, n+1) :
                elements.append(e)
                dfs(elements, e+1, k-1)
                elements.pop()
                
        dfs([], 1, k)
        return results
    
        # # itertools
        # return itertools.combinations(range(1, n+1), k)
