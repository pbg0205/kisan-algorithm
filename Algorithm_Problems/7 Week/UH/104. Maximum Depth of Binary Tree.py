"""
Runtime: 24 ms, faster than 99.97% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.5 MB, less than 79.81% of Python3 online submissions for Maximum Depth of Binary Tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        Q = collections.deque([root])
        depth = 0
        
        # BFS
        while Q :
            depth += 1
            for _ in range(len(Q)):
                cur_root = Q.popleft()
                if cur_root.left: 
                    Q.append(cur_root.left)
                if cur_root.right:
                    Q.append(cur_root.right)
        
        return depth
