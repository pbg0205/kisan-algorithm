"""
Runtime: 32 ms, faster than 62.96% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.2 MB, less than 46.05% of Python3 online submissions for Invert Binary Tree.

직접 풀었으며 책의 설명 방법보다 시간이 조금 느리다. BFS로 각 레벨을 순회하는 층별 순회로 코드 작성
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None :
            return root
        
        Q = collections.deque([root])
        
        #BFS
        while Q :
            for _ in range(len(Q)):
                node = Q.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            
        return root
      
      
"""
Runtime: 28 ms, faster than 86.51% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.3 MB, less than 46.05% of Python3 online submissions for Invert Binary Tree.
for문을 안스므로 조금 개선 조금은 이상한 순회
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None :
            return root
        
        Q = collections.deque([root])
        
        #BFS
        while Q :
            node = Q.popleft()
            if node:
                node.left, node.right = node.right, node.left
                Q.append(node.left)
                Q.append(node.right)
            
        return root
      
"""
스왑을 고려한 DFS 전위 순회 & 후위 순회
Runtime: 32 ms, faster than 62.96% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.2 MB, less than 74.80% of Python3 online submissions for Invert Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None :
            return root
        
        stack = collections.deque([root])
        
        #BFS
        while stack :
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
            
        return root
      
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None :
            return root
        
        stack = collections.deque([root])
        
        #BFS
        while stack :
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                node.left, node.right = node.right, node.left
        return root
      
"""
가장 파이토닉한 방법
Runtime: 32 ms, faster than 62.96% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.1 MB, less than 74.80% of Python3 online submissions for Invert Binary Tree.
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root :
            root.left, root.right = \
            self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None
      
    
