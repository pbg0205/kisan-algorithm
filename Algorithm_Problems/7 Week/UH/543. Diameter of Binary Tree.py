"""
Runtime: 40 ms, faster than 88.25% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 16.2 MB, less than 65.01% of Python3 online submissions for Diameter of Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(tree):
            if tree is None :
                return -1
            
            left = dfs(tree.left)
            right = dfs(tree.right)
            
            self.longest = max(self.longest, left+right+2)
            
            return max(left, right) + 1
        
        dfs(root)
        return self.longest
            
      
