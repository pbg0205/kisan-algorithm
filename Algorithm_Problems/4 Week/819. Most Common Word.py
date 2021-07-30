"""
Runtime: 40 ms, faster than 39.50% of Python3 online submissions for Most Common Word.
Memory Usage: 14.4 MB, less than 48.79% of Python3 online submissions for Most Common Word.
"""

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        return max(words, key = words.count)
      
# 내장 라이브러리 ma의 새로운 사용법!
