"""
Runtime: 32 ms, faster than 64.12% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 14.2 MB, less than 62.06% of Python3 online submissions for Letter Combinations of a Phone Number.
"""

"""
# 모든 수에 대한 조합 계산 (DFS)
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(idx, path):
            # ending condition
            if len(path) == len(digits):
                paths.append(path)
                return
            
            # search
            for i in range(idx, len(digits)):
                for j in char_dic[digits[i]]:
                    dfs(i+1, path+j)
        
        if not digits:
            return []
        
        char_dic = self.get_char_dic()
        paths = []
        dfs(0,'')
        return paths
    
    # 번호-문자 생성부
    @staticmethod
    def get_char_dic():
        char_dic = defaultdict(str)
        accumulate = 0
        for size, num in zip( [3,3,3,3,3,4,3,4], range(2,10)):
            for _ in range(0,size) :
                char_dic[str(num)] += chr(97+accumulate)
                accumulate+=1
        return char_dic
