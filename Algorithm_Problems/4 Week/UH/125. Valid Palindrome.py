"""
low memory & slow speed version

Runtime: 52 ms, faster than 47.45% of Python3 online submissions for Valid Palindrome.
Memory Usage: 14.6 MB, less than 62.86% of Python3 online submissions for Valid Palindrome.

투 포인트 접근

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        
        while left < right :
            while not s[left].isalnum():
                left += 1    
                if left >= len(s):
                    return True
            while not s[right].isalnum():
                right -= 1    
                    
            if s[left].lower() != s[right].lower():
                return False
            else :
                left += 1
                right -= 1
       
      
"""
high memory & fast speed version
Runtime: 40 ms, faster than 88.99% of Python3 online submissions for Valid Palindrome.
Memory Usage: 20.1 MB, less than 6.00% of Python3 online submissions for Valid Palindrome.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = [char.lower() for char in s if char.isalnum()]
        if new_s == new_s[::-1] :
            return True
        else:
            return False
        
