"""
책에 있는 재귀 구현
Runtime: 84 ms, faster than 76.24% of Python3 online submissions for Merge Two Binary Trees.
Memory Usage: 15.4 MB, less than 51.72% of Python3 online submissions for Merge Two Binary Trees.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node
        else :
            return root1 or root2
        
