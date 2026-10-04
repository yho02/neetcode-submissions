# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif root.right == None and root.left == None:
            return 1 
        else:
            return max(1 + self.maxDepth(root.right), 1 + self.maxDepth(root.left))
