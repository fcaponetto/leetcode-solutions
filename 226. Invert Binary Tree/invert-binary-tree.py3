# 226. Invert Binary Tree (2/20/56549)
# Runtime: 40 ms (17.13%) Memory: 16.57 MB (0.00%) 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        frontier = deque()
        if root:
            frontier.append(root)

        while frontier:
            for _ in range(len(frontier)): 
                curr = frontier.popleft()
                
                print(curr)
                left = curr.left
                right = curr.right
                if left:
                    frontier.append(left)
                if right:
                    frontier.append(right)

                curr.right = left
                curr.left = right

                
        return root
