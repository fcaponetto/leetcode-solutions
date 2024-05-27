# 112. Path Sum (16/07/56374)
# Runtime: 38 ms (70.01%) Memory: 17.31 MB (77.94%) 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, node, currentSum, targetSum):
        if not node:
            return False

        currentSum += node.val

        # Check if it's a leaf node and if the path sum equals targetSum
        if not node.left and not node.right:
            return currentSum == targetSum

        # Recur for left and right subtrees
        if self.helper(node.left, currentSum, targetSum):
            return True
        if self.helper(node.right, currentSum, targetSum):
            return True

        currentSum -= node.val

        return False
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, 0, targetSum)