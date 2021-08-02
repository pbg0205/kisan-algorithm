"""
Runtime: 36 ms, faster than 74.27% of Python3 online submissions for Reorder Data in Log Files.
Memory Usage: 14.3 MB, less than 65.55% of Python3 online submissions for Reorder Data in Log Files.
"""

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        
        for log in logs :
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        
        return letter_logs + digit_logs
        
