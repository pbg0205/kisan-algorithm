"""
Runtime: 88 ms, faster than 96.90% of Python3 online submissions for Group Anagrams.
Memory Usage: 17.2 MB, less than 85.45% of Python3 online submissions for Group Anagrams.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for key in strs :
            ordered_key = ''.join(sorted(key))
            if ordered_key in group:
                group[ordered_key] += [key]
            else:
                group[ordered_key] = [key]
        
        return [value for value in group.values()]
