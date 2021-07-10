"""
21.07.10
Runtime: 100 ms, faster than 73.35% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.9 MB, less than 31.84% of Python3 online submissions for Top K Frequent Elements.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1 <= nums.length <= 105
        # It is guaranteed that the answer is unique.
        
        # 단순 접근 : use Counter
        counter = collections.Counter(nums)
        # 답의 유일성 보장 활용
        return [num for num, _ in counter.most_common(k)] 
        
