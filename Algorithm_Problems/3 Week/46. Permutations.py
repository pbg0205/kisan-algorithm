
"""
Runtime: 32 ms, faster than 97.04% of Python3 online submissions for Permutations.
Memory Usage: 14.5 MB, less than 42.40% of Python3 online submissions for Permutations.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    # dfs 구현
        results = []
        prev_elements = []
        
        def dfs(elements):
            # ending condition
            if not elements:
                results.append(prev_elements.copy())
                    
            for e in elements :
                # 자식 요수 구성
                next_elements = elements.copy()
                next_elements.remove(e)
                
                # 부모 요소 결과 추가
                prev_elements.append(e)
                # 자식 재귀 호출
                dfs(next_elements)
                # 스택 활용 - 백트래킹
                prev_elements.pop()
                
        dfs(nums)
        
        return results
        
    
# # 라이브러리 
#         from itertools import permutations
#         return permutations(nums,3)
