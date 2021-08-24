"""
Runtime: 96 ms, faster than 98.42% of Python3 online submissions for Serialize and Deserialize Binary Tree.
Memory Usage: 18.8 MB, less than 79.25% of Python3 online submissions for Serialize and Deserialize Binary Tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    null_tag = "#"

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        route = []
        queue = collections.deque([root])
        while queue : 
            node = queue.popleft()
            if node:
                route.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else :
                route.append(self.null_tag)
        print(route)
        return route
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = collections.deque(data)
        
        root_val = nodes.popleft()
        
        if root_val != self.null_tag:
            root = TreeNode(root_val)
        else :
            return None
        
        queue = collections.deque([root])
        
        while queue:
            p_node = queue.popleft()
            left = nodes.popleft()
            right = nodes.popleft()
            
            if left != self.null_tag : 
                p_node.left = TreeNode(left)
                queue.append(p_node.left)
            
            if right != self.null_tag : 
                p_node.right = TreeNode(right)
                queue.append(p_node.right)
        
        
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
