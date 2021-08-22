"""Runtime: 380 ms, faster than 71.71% of Python3 online submissions for Longest Univalue Path.
Memory Usage: 18 MB, less than 39.58% of Python3 online submissions for Longest Univalue Path.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest = 0
    
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def dfs(tree, p_val):
            if tree is None:
                return -1
            
            left = dfs(tree.left, tree.val)
            right = dfs(tree.right, tree.val)
            
            self.longest = max(self.longest, left+right+2)
                
            return max(right, left)+1 if tree.val==p_val else -1
        
        dfs(root, root.val)
        
        return self.longest
        
