# 230. Kth Smallest Element in a BST (03/03/56380)
# Runtime: 40 ms (77.52%) Memory: 19.41 MB (57.75%) 

#    4
#   / \
#  2   5
#   \
#    3
# k=1 2 is is the 1st smallest element


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if not node:
                return
            
            # Traverse the left subtree
            inorder(node.left)
            
            # Process current node
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            
            # Traverse the right subtree
            inorder(node.right)
        
        self.count = 0
        self.result = None
        inorder(root)
        return self.result
